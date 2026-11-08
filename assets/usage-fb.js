/*
 * usage-fb.js — dependency-free FlatBuffers reader for assets/usage.fb
 * Layout matches scripts/usage.fbs (identifier "UEUG"):
 *   UsageBundle: version(slot0 int32), generated_at(slot1 str), docs(slot2 [UsageDoc])
 *   UsageDoc:    kind(0) slug(1) name(2) category(3) cn_steps(4 [str]) en_steps(5 [str]) note_cn(6) note_en(7)
 *
 * Usage:
 *   await UEUsage.load('/assets/usage.fb');
 *   const doc = UEUsage.get('module', 'aimodule');      // or UEUsage.getBySlug('aimodule')
 *   doc.name, doc.cn_steps (array), doc.en_steps (array), doc.note_cn ...
 */
(function (g) {
  'use strict';

  function Reader(buf) {
    this.dv = new DataView(buf);
    this.u8 = function (p) { return this.dv.getUint8(p); };
    this.u16 = function (p) { return this.dv.getUint16(p, true); };
    this.u32 = function (p) { return this.dv.getUint32(p, true); };
    this.i32 = function (p) { return this.dv.getInt32(p, true); };
    this.bytes = new Uint8Array(buf);
  }

  function fieldOffset(r, tbl, slot) {
    var vt = tbl - r.i32(tbl);
    var vtsize = r.u16(vt);
    var o = 4 + slot * 2;
    if (o >= vtsize) return 0;
    return r.u16(vt + o);
  }

  function readStr(r, tbl, slot) {
    var fo = fieldOffset(r, tbl, slot);
    if (fo === 0) return '';
    var pos = tbl + fo;
    var sp = pos + r.u32(pos);
    var n = r.u32(sp);
    var s = '';
    for (var i = 0; i < n; i++) s += String.fromCharCode(r.u8(sp + 4 + i));
    // decode UTF-8 (handles CJK)
    try {
      return decodeURIComponent(escape(s));
    } catch (e) {
      return s;
    }
  }

  function readVecStr(r, tbl, slot) {
    var fo = fieldOffset(r, tbl, slot);
    if (fo === 0) return [];
    var pos = tbl + fo;
    var vec = pos + r.u32(pos);
    var n = r.u32(vec);
    var out = [];
    for (var i = 0; i < n; i++) {
      var ep = vec + 4 + i * 4;
      var sp = ep + r.u32(ep);
      var len = r.u32(sp);
      var s = '';
      for (var j = 0; j < len; j++) s += String.fromCharCode(r.u8(sp + 4 + j));
      try { out.push(decodeURIComponent(escape(s))); } catch (e) { out.push(s); }
    }
    return out;
  }

  function readVecTable(r, tbl, slot) {
    var fo = fieldOffset(r, tbl, slot);
    if (fo === 0) return [];
    var pos = tbl + fo;
    var vec = pos + r.u32(pos);
    var n = r.u32(vec);
    var out = [];
    for (var i = 0; i < n; i++) {
      var ep = vec + 4 + i * 4;
      out.push(ep + r.u32(ep));
    }
    return out;
  }

  function readDoc(r, tbl) {
    return {
      kind: readStr(r, tbl, 0),
      slug: readStr(r, tbl, 1),
      name: readStr(r, tbl, 2),
      category: readStr(r, tbl, 3),
      cn_steps: readVecStr(r, tbl, 4),
      en_steps: readVecStr(r, tbl, 5),
      note_cn: readStr(r, tbl, 6),
      note_en: readStr(r, tbl, 7)
    };
  }

  var state = { bundle: null, index: null };

  function parse(arrayBuffer) {
    var r = new Reader(arrayBuffer);
    var ident = '';
    for (var i = 4; i < 8; i++) ident += String.fromCharCode(r.u8(i));
    if (ident !== 'UEUG') throw new Error('usage.fb: bad identifier ' + ident);
    var root = r.u32(0);
    var version = 0, fo = fieldOffset(r, root, 0);
    if (fo) version = r.i32(root + fo);
    var generatedAt = readStr(r, root, 1);
    var tables = readVecTable(r, root, 2);
    var docs = tables.map(function (t) { return readDoc(r, t); });
    var index = {};
    for (var k = 0; k < docs.length; k++) {
      var d = docs[k];
      index[d.kind + ':' + d.slug] = d;
    }
    state.bundle = { version: version, generated_at: generatedAt, docs: docs };
    state.index = index;
    return state.bundle;
  }

  var UEUsage = {
    parse: parse,
    load: function (url) {
      return fetch(url)
        .then(function (resp) {
          if (!resp.ok) throw new Error('fetch ' + url + ' -> ' + resp.status);
          return resp.arrayBuffer();
        })
        .then(parse);
    },
    get: function (kind, slug) {
      return state.index ? (state.index[kind + ':' + slug] || null) : null;
    },
    getBySlug: function (slug) {
      if (!state.index) return null;
      var k = 'plugin:' + slug;
      if (state.index[k]) return state.index[k];
      return state.index['module:' + slug] || null;
    },
    bundle: function () { return state.bundle; },
    count: function () { return state.bundle ? state.bundle.docs.length : 0; }
  };

  if (typeof module !== 'undefined' && module.exports) module.exports = UEUsage;
  g.UEUsage = UEUsage;
})(typeof globalThis !== 'undefined' ? globalThis : this);

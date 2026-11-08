async function e({kind:e,slug:t,message:n,history:r=[]},i={}){let{onChunk:a,onDone:o,onError:s}=i;try{let i=await fetch(`/api/ai/stream`,{method:`POST`,headers:{"Content-Type":`application/json`},body:JSON.stringify({kind:e,slug:t,message:n,history:r})});if(!i.ok||!i.body){let e=await i.text();throw Error(`HTTP ${i.status}: ${e.slice(0,300)}`)}let s=i.body.getReader(),c=new TextDecoder(`utf-8`),l=``;for(;;){let{value:e,done:t}=await s.read();if(t)break;l+=c.decode(e,{stream:!0}).replace(/\r\n/g,`
`);let n;for(;(n=l.indexOf(`

`))!==-1;){let e=l.slice(0,n);l=l.slice(n+2);for(let t of e.split(`
`)){if(!t.startsWith(`data:`))continue;let e=t.slice(5).replace(/^ /,``);if(e===`[DONE]`){o?.();return}a?.(JSON.parse(e))}}}o?.()}catch(e){s?.(e)}}async function t(e,t={},n={}){let{onFrame:r,onDone:i,onError:a}=t;try{let t=await fetch(`/api/ai/batch`,{method:`POST`,headers:{"Content-Type":`application/json`},body:JSON.stringify(e),...n});if(!t.ok||!t.body){let e=await t.text();throw Error(`HTTP ${t.status}: ${e.slice(0,300)}`)}let a=t.body.getReader(),o=new TextDecoder(`utf-8`),s=``;for(;;){let{value:e,done:t}=await a.read();if(t)break;s+=o.decode(e,{stream:!0}).replace(/\r\n/g,`
`);let n;for(;(n=s.indexOf(`

`))!==-1;){let e=s.slice(0,n);s=s.slice(n+2);for(let t of e.split(`
`)){if(!t.startsWith(`data:`))continue;let e=t.slice(5).replace(/^ /,``);if(e===`[DONE]`){i?.();return}r?.(JSON.parse(e))}}}i?.()}catch(e){a?.(e)}}export{t as n,e as t};
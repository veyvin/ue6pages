## 启用插件

在编辑器中打开 **Edit → Plugins**，搜索 `Aurora Sky` 并勾选启用，然后重启编辑器。

## 添加到关卡

1. 在放置面板搜索 `AuroraSkyActor`
2. 拖入关卡并调整 `Time of Day`
3. 在细节面板中开启 `Volumetric Clouds`

```cpp
#include "AuroraSkyActor.h"

void AMyLevel::SpawnSky()
{
    GetWorld()->SpawnActor<AAuroraSkyActor>();
}
```

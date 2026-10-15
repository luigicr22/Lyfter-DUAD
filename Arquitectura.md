## Arquitectura General

```mermaid
flowchart TD
    RP["Reloj de Marcas"]
    AR["API Reloj"]
    ADB["API Marcas"]
    DBM[("DB Marcas")]
    AA["API APP"]
    AM["APP Marcas"]
    
    WA["Web Administración"]
    ATR["API Trámite y Registro"]
    DBTR[("DB Trámite y Registro")]
    WF["Web Funcionarios"]


subgraph Marcas
    RP --- AR
    AR --- ADB
    ADB --- AA    
    AA --- AM
    ADB --- DBM
    subgraph DMZ
    AM
    end
end
subgraph Administracion
	WA --- ATR
	WF --- ATR
	ATR --- DBTR
	ATR --- ADB	
end

class RP,AR internal-link;
```
### Reloj vs App Movil
|	|Reloj |App Movil|
|------|------|------|
|Camaras usadas|Camara normal + camara Infraroja para verificar profundidad|Camara normal solamente|
|Identificación|Rostros con movimiento (espera patrones como parpadeo para verificar)|Se puede engañar con fotos o video llamadas (FaceId solamente esta disponible para desbloquear celular)|
|Usos|Verificación 1:N (1 reloj contra N usuarios)|Verifica 1:1 (Acceso por medio de FaceId)

### Reloj de Marcas

Las dos formas de integrarse

|              | Pull (SDK zkemkeeper)                    | Push (ADMS / iClock)                                      |
| ------------ | ---------------------------------------- | --------------------------------------------------------- |
| Quién inicia | Su servidor se conecta al reloj          | El reloj llama a su servidor                              |
| Dónde corre  | Solo Windows (COM)                       | Cualquier servidor HTTP (ASP.NET Core)                    |
| Red          | El reloj debe ser alcanzable (LAN o VPN) | El reloj solo necesita salir hacia su servidor            |
| Tiempo real  | No, por sondeo periódico                 | Casi inmediato                                            |
| Modelo       | MB360                                    | Solo aplicable para modelos KF160, 460 - MB160, 360, 460) |


| Marcas                               | Modelos                         |
| ------------------------------------ | ------------------------------- |
| [ZKteco](https://www.zkteco.com/en/) | [Reloj de Marcas](https://es.scribd.com/document/476568909/BIOMETRICO-MB360-pdf) |


### API Reloj

| Protocolo | Documentacion                                                                                                                                |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Push      | [PUSH Communication Protocol Manual](https://studylib.net/doc/27718586/ilide.info-attendance-push-communication-protocol-2020032...?p=5) |
| Pull      | [API Reloj - ZKBioModule SDK.pdf](https://es.scribd.com/document/651682355/ZKBioModule-SDK-for-Windows)|

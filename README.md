# Cadáver Exquisito

**Tabla de Contenidos**

- [Ejecutar la aplicación](#ejecutar-la-aplicación)
    - [Construir las imágines](#construir-las-imágenes)
    - [Correr la aplicación](#correr-la-aplicación)
- [Desarrollar](#desarrollar)

## Ejecutar la aplicación

### Construir las imágenes

La aplicación se ejecuta usango [Docker Compose](https://docs.docker.com/compose/). Si no lo tenés instalado, podés instalarlo
siguiendo [estas instrucciones](https://docs.docker.com/compose/install).

Una vez tengas Docker Compose, vas a necesitar generar las imágenes para el servidor y la UI. Para eso, ejecutá:

```bash
make images
```

### Correr la aplicación

Luego, podés poner a correr la aplicación con el siguiente comando:

```bash
make api
```

## Desarrollar

Para desarrollar nuevas funcionalidades dentro de la aplicación es posible usar un contenedor
de desarrollo. Para eso, abrir el proyecto en [VSCode](https://code.visualstudio.com/), presionar
`ctrl + shift + p` y seleccionar `Dev Containers: Reopen in Container`.

Esto también es posible en otros editores de código como
[PyCharm](https://www.jetbrains.com/help/pycharm/getting-started.html) siguiendo las instrucciones
particulares.

Una vez instaladas las dependencias dentro del contenedor, es posible poner a correr la aplicación
directamente desde el `Debugger`. Allí se encuentran las siguientes opciones:

- `Server`: pone a correr el servidor o _back-end_.
- `UI`: pone a correr la UI o _front-end_.
- `API`: ejecuta en simultáneo el servidor y la UI, cada uno en una consola por separado.

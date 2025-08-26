#  Sistema de Gestión de Tareas

##  Descripción
Este proyecto implementa un **Sistema de Gestión de Tareas** utilizando el **Patrón de Diseño Command** en **Python**. 
Permite realizar operaciones como **crear, editar, eliminar y completar tareas**, con la posibilidad de deshacer cada acción gracias al registro de comandos ejecutados.

##  Objetivo
Facilitar la gestión de tareas con una arquitectura escalable y desacoplada, permitiendo agregar nuevas funcionalidades sin modificar el código base.

##  Patrón de Diseño Utilizado: Command
El **Command Pattern** encapsula cada acción del usuario en un objeto de comando separado. Esto ofrece los siguientes beneficios:
-  **Desacopla** el invocador de los objetos que ejecutan las acciones.
-  **Permite la extensión** de nuevas operaciones sin modificar el código existente.
-  **Facilita la reversión** de operaciones gracias al registro de comandos ejecutados.

##  Arquitectura del Sistema
El sistema sigue una estructura modular con las siguientes clases:

### ** Clases Principales**
- **`Tarea`**: Representa una tarea con título, descripción y estado de completado.
- **`Comando` (Abstracta)**: Define la interfaz base para todos los comandos.
- **`CrearTareaCommand`**: Crea una nueva tarea.
- **`EditarTareaCommand`**: Modifica el título y descripción de una tarea existente.
- **`EliminarTareaCommand`**: Elimina una tarea.
- **`CompletarTareaCommand`**: Marca una tarea como completada.
- **`GestorComandos`**: Administra la ejecución y reversión de los comandos.

##  Diagrama de Clases:

```mermaid
classDiagram
    class Tarea {
        - string titulo
        - string descripcion
        - bool completada
        + completar()
    }
    
    class Comando {
        <<interface>>
        + ejecutar()
        + deshacer()
    }
    
    class CrearTareaCommand {
        - Tarea tarea
        + ejecutar()
        + deshacer()
    }
    
    class EditarTareaCommand {
        - Tarea tarea
        - string titulo_anterior
        - string descripcion_anterior
        + ejecutar()
        + deshacer()
    }
    
    class CompletarTareaCommand {
        - Tarea tarea
        + ejecutar()
        + deshacer()
    }
    
    class EliminarTareaCommand {
        - Tarea tarea
        + ejecutar()
        + deshacer()
    }
    
    class GestorComandos {
        - list historial
        + ejecutar_comando(Comando cmd)
        + deshacer_comando()
    }
    
    Comando <|-- CrearTareaCommand
    Comando <|-- EditarTareaCommand
    Comando <|-- CompletarTareaCommand
    Comando <|-- EliminarTareaCommand
    
    GestorComandos --> Comando
    CrearTareaCommand --> Tarea
    EditarTareaCommand --> Tarea
    CompletarTareaCommand --> Tarea
    EliminarTareaCommand --> Tarea

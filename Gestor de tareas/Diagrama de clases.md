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

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Tarea:
    """Representa una tarea con título, descripción y estado de completado."""
    titulo: str
    descripcion: str
    completada: bool = False

    def completar(self) -> None:
        """Marca la tarea como completada."""
        self.completada = True

    def editar(self, nuevo_titulo: str, nueva_descripcion: str) -> None:
        """Edita el título y la descripción de la tarea."""
        self.titulo = nuevo_titulo
        self.descripcion = nueva_descripcion


class Comando(ABC):
    """Interfaz base para los comandos."""
    
    @abstractmethod
    def ejecutar(self) -> None:
        pass

    @abstractmethod
    def deshacer(self) -> None:
        pass


class CrearTareaCommand(Comando):
    """Comando para crear una tarea."""
    
    def __init__(self, gestor: "GestorComandos", tarea: Tarea) -> None:
        self.gestor = gestor
        self.tarea = tarea

    def ejecutar(self) -> None:
        self.gestor.agregar_tarea(self.tarea)

    def deshacer(self) -> None:
        self.gestor.eliminar_tarea(self.tarea)


class EditarTareaCommand(Comando):
    """Comando para editar una tarea."""
    
    def __init__(self, tarea: Tarea, nuevo_titulo: str, nueva_descripcion: str) -> None:
        self.tarea = tarea
        self.nuevo_titulo = nuevo_titulo
        self.nueva_descripcion = nueva_descripcion
        self.titulo_anterior = tarea.titulo
        self.descripcion_anterior = tarea.descripcion

    def ejecutar(self) -> None:
        self.tarea.editar(self.nuevo_titulo, self.nueva_descripcion)

    def deshacer(self) -> None:
        self.tarea.editar(self.titulo_anterior, self.descripcion_anterior)


class EliminarTareaCommand(Comando):
    """Comando para eliminar una tarea."""
    
    def __init__(self, gestor: "GestorComandos", tarea: Tarea) -> None:
        self.gestor = gestor
        self.tarea = tarea

    def ejecutar(self) -> None:
        self.gestor.eliminar_tarea(self.tarea)

    def deshacer(self) -> None:
        self.gestor.agregar_tarea(self.tarea)


class CompletarTareaCommand(Comando):
    """Comando para completar una tarea."""
    
    def __init__(self, tarea: Tarea) -> None:
        self.tarea = tarea

    def ejecutar(self) -> None:
        self.tarea.completar()

    def deshacer(self) -> None:
        self.tarea.completada = False


class GestorComandos:
    """Gestor que administra la ejecución y reversión de comandos."""
    
    def __init__(self) -> None:
        self.historial: List[Comando] = []
        self.tareas: List[Tarea] = []

    def ejecutar_comando(self, comando: Comando) -> None:
        """Ejecuta un comando y lo almacena en el historial."""
        comando.ejecutar()
        self.historial.append(comando)

    def deshacer_comando(self) -> None:
        """Deshace el último comando ejecutado."""
        if self.historial:
            comando = self.historial.pop()
            comando.deshacer()

    def agregar_tarea(self, tarea: Tarea) -> None:
        """Añade una tarea a la lista de tareas."""
        self.tareas.append(tarea)

    def eliminar_tarea(self, tarea: Tarea) -> None:
        """Elimina una tarea de la lista de tareas."""
        if tarea in self.tareas:
            self.tareas.remove(tarea)

    def listar_tareas(self) -> None:
        """Lista todas las tareas registradas."""
        if not self.tareas:
            print("\n📌 No hay tareas registradas.")
            return
        print("\n📋 Lista de Tareas:")
        for i, tarea in enumerate(self.tareas):
            estado = "✔️ Completada" if tarea.completada else "❌ Pendiente"
            print(f"{i + 1}. {tarea.titulo} - {tarea.descripcion} ({estado})")


# ---------------------- Menú Interactivo ---------------------- #
def menu():
    gestor = GestorComandos()

    while True:
        print("\n📌 MENÚ DE GESTIÓN DE TAREAS 📌")
        print("1️⃣  Crear tarea")
        print("2️⃣  Completar tarea")
        print("3️⃣  Editar tarea")
        print("4️⃣  Eliminar tarea")
        print("5️⃣  Listar tareas")
        print("6️⃣  Deshacer última acción")
        print("0️⃣  Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            titulo = input("📌 Ingrese el título de la tarea: ")
            descripcion = input("✍️ Ingrese la descripción: ")
            tarea = Tarea(titulo, descripcion)
            gestor.ejecutar_comando(CrearTareaCommand(gestor, tarea))
            print("✅ Tarea creada con éxito.")

        elif opcion == "2":
            gestor.listar_tareas()
            index = int(input("📌 Ingrese el número de la tarea a completar: ")) - 1
            if 0 <= index < len(gestor.tareas):
                gestor.ejecutar_comando(CompletarTareaCommand(gestor.tareas[index]))
                print("✅ Tarea completada.")
            else:
                print("❌ Número de tarea inválido.")

        elif opcion == "3":
            gestor.listar_tareas()
            index = int(input("📌 Ingrese el número de la tarea a editar: ")) - 1
            if 0 <= index < len(gestor.tareas):
                nuevo_titulo = input("✏️ Nuevo título: ")
                nueva_descripcion = input("📝 Nueva descripción: ")
                gestor.ejecutar_comando(EditarTareaCommand(gestor.tareas[index], nuevo_titulo, nueva_descripcion))
                print("✅ Tarea editada con éxito.")
            else:
                print("❌ Número de tarea inválido.")

        elif opcion == "4":
            gestor.listar_tareas()
            index = int(input("📌 Ingrese el número de la tarea a eliminar: ")) - 1
            if 0 <= index < len(gestor.tareas):
                gestor.ejecutar_comando(EliminarTareaCommand(gestor, gestor.tareas[index]))
                print("🗑️ Tarea eliminada.")
            else:
                print("❌ Número de tarea inválido.")

        elif opcion == "5":
            gestor.listar_tareas()

        elif opcion == "6":
            gestor.deshacer_comando()
            print("⏪ Última acción deshecha.")

        elif opcion == "0":
            print("👋 ¡Hasta luego!")
            break

        else:
            print("❌ Opción inválida. Intente de nuevo.")


# Ejecutar el menú
if __name__ == "__main__":
    menu()


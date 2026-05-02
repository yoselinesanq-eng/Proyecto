import streamlit as st
import numpy as np
import pandas as pd
# ---------------------------------------------------------
# CONFIGURACIÓN GENERAL DE LA APLICACIÓN
# ---------------------------------------------------------
st.set_page_config(
    page_title="Proyecto Python - Módulo 1",

    layout="centered"
)

# ---------------------------------------------------------
# MENÚ LATERAL
# ---------------------------------------------------------
menu = st.sidebar.selectbox(
    "Navegación",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
)

# ---------------------------------------------------------
# SECCIÓN HOME
# ---------------------------------------------------------
if menu == "Home":
    st.title("Proyecto Final – Módulo 1: Fundamentos de Python")
    st.subheader("Aplicación Interactiva en Streamlit")

    # Logo o imagen representativa
    st.image(
        "C:\\Users\\Yoseline\\Downloads\\Trabajo\\Logo.png",
        width=250
    )

    st.markdown("## Estudiante")
    st.write("**Nombre completo:** Yoseline Carolina Sanchez Quino")
    st.write("**Módulo:** Fundamentos de Programación en Python – Módulo 1")
    st.write("**Año:** 2026")

    st.markdown("##Descripción del Proyecto")
    st.write("""
    Esta aplicación interactiva ha sido desarrollada como parte del proyecto final del Módulo 1 del curso de Python.
    Integra los conceptos fundamentales aprendidos, incluyendo:
    - Variables  
    - Estructuras de datos  
    - Control de flujo  
    - Funciones  
    - Programación funcional  
    - Programación orientada a objetos (POO)  
    """)

    st.markdown("## Tecnologías Utilizadas")
    st.write("""
    - **Python 3**
    - **Streamlit**
    - Programación funcional
    - Programación orientada a objetos
    """)

    st.success("Bienvenido a la aplicación. Usa el menú lateral para navegar por los ejercicios.")
elif menu == "Ejercicio 1":
    st.title("Ejercicio 1 – Flujo de Caja con Listas")
    st.markdown("""
    En este ejercicio registraremos movimientos financieros usando una lista.
    Cada movimiento tendrá:
    - Concepto  
    - Tipo de movimiento (Ingreso o Gasto)  
    - Valor  

    Luego mostraremos:
    - Lista de movimientos  
    - Total de ingresos  
    - Total de gastos  
    - Saldo final  
    - Estado del flujo de caja  
    """)

    # ---------------------------------------------------------
    # Inicializar lista en sesión
    # ---------------------------------------------------------
    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    # ---------------------------------------------------------
    # FORMULARIO DE REGISTRO
    # ---------------------------------------------------------
    st.subheader("Registrar movimiento")

    concepto = st.text_input("Concepto del movimiento")
    tipo = st.selectbox("Tipo de movimiento", ["Ingreso", "Gasto"])
    valor = st.number_input("Valor", min_value=0.0, step=0.1)

    if st.button("Agregar movimiento"):
        if concepto.strip() == "" or valor == 0:
            st.error("Debe ingresar un concepto válido y un valor mayor a 0.")
        else:
            st.session_state.movimientos.append({
                "concepto": concepto,
                "tipo": tipo,
                "valor": valor
            })
            st.success("Movimiento agregado correctamente.")

    # ---------------------------------------------------------
    # MOSTRAR TABLA DE MOVIMIENTOS
    # ---------------------------------------------------------
    st.subheader("Movimientos registrados")

    if len(st.session_state.movimientos) > 0:
        st.dataframe(st.session_state.movimientos)

        # ---------------------------------------------------------
        # CÁLCULOS
        # ---------------------------------------------------------
        total_ingresos = sum(m["valor"] for m in st.session_state.movimientos if m["tipo"] == "Ingreso")
        total_gastos = sum(m["valor"] for m in st.session_state.movimientos if m["tipo"] == "Gasto")
        saldo_final = total_ingresos - total_gastos

        # ---------------------------------------------------------
        # MÉTRICAS
        # ---------------------------------------------------------
        st.subheader("Resumen del flujo de caja")
        col1, col2, col3 = st.columns(3)

        col1.metric("Total Ingresos", f"S/ {total_ingresos:.2f}")
        col2.metric("Total Gastos", f"S/ {total_gastos:.2f}")
        col3.metric("Saldo Final", f"S/ {saldo_final:.2f}")

        # ---------------------------------------------------------
        # ESTADO DEL FLUJO
        # ---------------------------------------------------------
        if saldo_final > 0:
            st.success("El flujo de caja está **a favor**.")
        elif saldo_final < 0:
            st.error("El flujo de caja está **en contra**.")
        else:
            st.info("El flujo de caja está **equilibrado**.")
    else:
        st.info("Aún no se han registrado movimientos.")

#Ejercicio 2

elif menu == "Ejercicio 2":


    st.title("Ejercicio 2 – Registro con NumPy y DataFrame")

    st.markdown("""
    En este ejercicio registraremos productos usando **arreglos de NumPy**.
    Cada registro contiene:
    - Nombre del producto  
    - Categoría  
    - Precio  
    - Cantidad  
    - Total (precio × cantidad)  

    Los registros se almacenan en arrays y luego se muestran en un DataFrame.
    """)

    # ---------------------------------------------------------
    # Inicializar arrays en session_state
    # ---------------------------------------------------------
    if "productos" not in st.session_state:
        st.session_state.productos = np.array([])      # nombre
        st.session_state.categorias = np.array([])     # categoría
        st.session_state.precios = np.array([])        # precio
        st.session_state.cantidades = np.array([])     # cantidad
        st.session_state.totales = np.array([])        # total

    # ---------------------------------------------------------
    # FORMULARIO DE REGISTRO
    # ---------------------------------------------------------
    st.subheader("Registrar nuevo producto")

    nombre = st.text_input("Nombre del producto")
    categoria = st.selectbox("Categoría", ["Tecnología", "Hogar", "Ropa", "Alimentos", "Otros"])
    precio = st.number_input("Precio", min_value=0.0, step=0.1)
    cantidad = st.number_input("Cantidad", min_value=0, step=1)

    if st.button("Agregar registro"):
        if nombre.strip() == "" or precio == 0 or cantidad == 0:
            st.error("Debe ingresar un nombre válido, precio mayor a 0 y cantidad mayor a 0.")
        else:
            total = precio * cantidad

            # Agregar a los arrays
            st.session_state.productos = np.append(st.session_state.productos, nombre)
            st.session_state.categorias = np.append(st.session_state.categorias, categoria)
            st.session_state.precios = np.append(st.session_state.precios, precio)
            st.session_state.cantidades = np.append(st.session_state.cantidades, cantidad)
            st.session_state.totales = np.append(st.session_state.totales, total)

            st.success("Registro agregado correctamente.")

    # ---------------------------------------------------------
    # MOSTRAR DATAFRAME
    # ---------------------------------------------------------
    st.subheader("Tabla de registros")

    if len(st.session_state.productos) > 0:
        df = pd.DataFrame({
            "Producto": st.session_state.productos,
            "Categoría": st.session_state.categorias,
            "Precio": st.session_state.precios,
            "Cantidad": st.session_state.cantidades,
            "Total": st.session_state.totales
        })

        st.dataframe(df)

    else:
        st.info("Aún no se han registrado productos.")

#Ejecicio 3

elif menu == "Ejercicio 3":

    st.title("Ejercicio 3 – Uso de Funciones desde una Librería Externa")

    st.markdown("""
    En este ejercicio se utiliza una **función externa** para calcular el  
    **Índice de Masa Corporal (IMC)**.  
    El usuario ingresa los parámetros, ejecuta la función y se guarda un  
    **histórico de resultados** en un DataFrame.
    """)

    # ---------------------------------------------------------
    # Funciones externas (simulan librería importada)
    # ---------------------------------------------------------
    def validar_positivo(valor, nombre):
        if valor <= 0:
            raise ValueError(f"El valor de {nombre} debe ser positivo.")

    def calcular_imc(peso_kg: float, altura_m: float) -> dict:
        validar_positivo(peso_kg, "peso_kg")
        validar_positivo(altura_m, "altura_m")

        imc = peso_kg / (altura_m ** 2)

        if imc < 18.5:
            clasificacion = "Bajo peso"
        elif imc < 25:
            clasificacion = "Peso normal"
        elif imc < 30:
            clasificacion = "Sobrepeso"
        else:
            clasificacion = "Obesidad"

        return {
            "imc": round(imc, 2),
            "clasificacion": clasificacion
        }

    # ---------------------------------------------------------
    # Inicializar histórico
    # ---------------------------------------------------------
    if "historial_imc" not in st.session_state:
        st.session_state.historial_imc = []

    # ---------------------------------------------------------
    # Selector de función (requisito del ejercicio)
    # ---------------------------------------------------------
    st.subheader("Seleccionar función")

    funcion_seleccionada = st.selectbox(
        "Seleccione la función a ejecutar:",
        ["Calcular IMC"]
    )

    # ---------------------------------------------------------
    # Widgets para ingresar parámetros
    # ---------------------------------------------------------
    st.subheader("Ingresar parámetros")

    peso = st.number_input("Peso (kg)", min_value=0.0, step=0.1)
    altura = st.number_input("Altura (m)", min_value=0.0, step=0.01)

    # ---------------------------------------------------------
    # Botón para ejecutar
    # ---------------------------------------------------------
    if st.button("Ejecutar función"):
        try:
            if funcion_seleccionada == "Calcular IMC":
                resultado = calcular_imc(peso, altura)

                st.success("Función ejecutada correctamente.")
                st.write("### Resultado:")
                st.write(f"**IMC:** {resultado['imc']}")
                st.write(f"**Clasificación:** {resultado['clasificacion']}")

                # Guardar en histórico
                st.session_state.historial_imc.append({
                    "peso": peso,
                    "altura": altura,
                    "imc": resultado["imc"],
                    "clasificacion": resultado["clasificacion"]
                })

        except Exception as e:
            st.error(f"Error: {str(e)}")

    # ---------------------------------------------------------
    # Mostrar histórico
    # ---------------------------------------------------------
    st.subheader("Histórico de resultados")

    if len(st.session_state.historial_imc) > 0:
        df = pd.DataFrame(st.session_state.historial_imc)
        st.dataframe(df)
    else:
        st.info("Aún no hay resultados registrados.")

#Ejercicio 4

elif menu == "Ejercicio 4":
    import math
    import pandas as pd

    st.title("Ejercicio 4 – Uso de Clases con CRUD (POO)")

    st.markdown("""
    En este ejercicio se utiliza la clase **Paciente** desde una librería externa.  
    Se implementa un sistema **CRUD**:
    - Crear pacientes  
    - Leer registros  
    - Actualizar pacientes  
    - Eliminar pacientes  
    """)

    # ---------------------------------------------------------
    # Funciones externas (simulan librería importada)
    # ---------------------------------------------------------
    def validar_positivo(valor, nombre):
        if valor <= 0:
            raise ValueError(f"El valor de {nombre} debe ser positivo.")

    class Paciente:
        """
        Representa un paciente para cálculos básicos educativos
        como IMC y superficie corporal.
        """

        def __init__(self, nombre, peso_kg, altura_m):
            self.nombre = nombre
            self.peso_kg = peso_kg
            self.altura_m = altura_m

            validar_positivo(self.peso_kg, "peso_kg")
            validar_positivo(self.altura_m, "altura_m")

        def calcular_imc(self):
            return self.peso_kg / (self.altura_m ** 2)

        def clasificacion_imc(self):
            imc = self.calcular_imc()

            if imc < 18.5:
                return "Bajo peso"
            elif imc < 25:
                return "Peso normal"
            elif imc < 30:
                return "Sobrepeso"
            return "Obesidad"

        def calcular_superficie_corporal(self):
            altura_cm = self.altura_m * 100
            return math.sqrt((self.peso_kg * altura_cm) / 3600)

        def resumen(self):
            return {
                "paciente": self.nombre,
                "peso_kg": self.peso_kg,
                "altura_m": self.altura_m,
                "imc": round(self.calcular_imc(), 2),
                "clasificacion_imc": self.clasificacion_imc(),
                "superficie_corporal_m2": round(self.calcular_superficie_corporal(), 3)
            }

    # ---------------------------------------------------------
    # Inicializar lista de pacientes
    # ---------------------------------------------------------
    if "pacientes" not in st.session_state:
        st.session_state.pacientes = []   # lista de objetos Paciente

    # ---------------------------------------------------------
    # TABS CRUD
    # ---------------------------------------------------------
    tab1, tab2, tab3, tab4 = st.tabs(["Crear", "Leer", "Actualizar", "Eliminar"])

    # ---------------------------------------------------------
    # TAB CREAR
    # ---------------------------------------------------------
    with tab1:
        st.subheader("Crear nuevo paciente")

        nombre = st.text_input("Nombre del paciente")
        peso = st.number_input("Peso (kg)", min_value=0.0, step=0.1)
        altura = st.number_input("Altura (m)", min_value=0.0, step=0.01)

        if st.button("Agregar paciente"):
            try:
                paciente = Paciente(nombre, peso, altura)
                st.session_state.pacientes.append(paciente)
                st.success("Paciente agregado correctamente.")
            except Exception as e:
                st.error(f"Error: {str(e)}")

    # ---------------------------------------------------------
    # TAB LEER
    # ---------------------------------------------------------
    with tab2:
        st.subheader("Lista de pacientes")

        if len(st.session_state.pacientes) > 0:
            df = pd.DataFrame([p.resumen() for p in st.session_state.pacientes])
            st.dataframe(df)
        else:
            st.info("No hay pacientes registrados.")

    # ---------------------------------------------------------
    # TAB ACTUALIZAR
    # ---------------------------------------------------------
    with tab3:
        st.subheader("Actualizar paciente")

        if len(st.session_state.pacientes) == 0:
            st.info("No hay pacientes para actualizar.")
        else:
            nombres = [p.nombre for p in st.session_state.pacientes]
            seleccionado = st.selectbox("Seleccione un paciente", nombres)

            paciente = next(p for p in st.session_state.pacientes if p.nombre == seleccionado)

            nuevo_peso = st.number_input("Nuevo peso (kg)", min_value=0.0, step=0.1, value=paciente.peso_kg)
            nueva_altura = st.number_input("Nueva altura (m)", min_value=0.0, step=0.01, value=paciente.altura_m)

            if st.button("Actualizar"):
                try:
                    paciente.peso_kg = nuevo_peso
                    paciente.altura_m = nueva_altura
                    validar_positivo(paciente.peso_kg, "peso_kg")
                    validar_positivo(paciente.altura_m, "altura_m")
                    st.success("Paciente actualizado correctamente.")
                except Exception as e:
                    st.error(f"Error: {str(e)}")

    # ---------------------------------------------------------
    # TAB ELIMINAR
    # ---------------------------------------------------------
    with tab4:
        st.subheader("Eliminar paciente")

        if len(st.session_state.pacientes) == 0:
            st.info("No hay pacientes para eliminar.")
        else:
            nombres = [p.nombre for p in st.session_state.pacientes]
            seleccionado = st.selectbox("Seleccione un paciente a eliminar", nombres)

            if st.button("Eliminar"):
                st.session_state.pacientes = [
                    p for p in st.session_state.pacientes if p.nombre != seleccionado
                ]
                st.success("Paciente eliminado correctamente.")

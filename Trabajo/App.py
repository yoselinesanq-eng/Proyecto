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
        "data:image/png;base64,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",
        width=250
    )

    # st.markdown("## Estudiante")
    st.write("**Nombre completo:** Yoseline Carolina Sanchez Quino")
    st.write("**Módulo:** Fundamentos de Programación en Python – Módulo 1")
    st.write("**Año:** 2026")

    st.markdown("## Descripción del Proyecto")
    st.write("""
    Esta aplicación interactiva ha sido desarrollada como parte del trabajo práctico del Módulo 1 del curso de Python.
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
    - **Programación funcional**
    - **Programación orientada a objetos**
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
                st.write(f"**Clasificacion:** {resultado['clasificacion']}")

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

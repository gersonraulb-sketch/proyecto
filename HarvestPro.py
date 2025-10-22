class Cosecha:
    cosechas = []

    def __init__(self, fecha, tipo, cantidad, temporada):
        self.fecha = fecha
        self.tipo = tipo
        self.cantidad = cantidad
        self.temporada = temporada

    @classmethod
    def agregar_cosecha(cls, fecha, tipo, cantidad, temporada):
        nueva_c = Cosecha(fecha, tipo, cantidad, temporada)
        cls.cosechas.append(nueva_c)
        cls.guardar_en_bd(nueva_c)

    @staticmethod
    def guardar_en_bd(cosecha):
        try:
            from conexion import conn
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO cult (fecha, tipo, cantidad, temporada) VALUES (%s, %s, %s, %s)",
                (cosecha.fecha, cosecha.tipo, cosecha.cantidad, cosecha.temporada)
            )
            conn.commit()
            cursor.close()
            conn.close()
            print("Cosecha guardada correctamente en la base de datos.")
        except:
            print("Error al guardar en la base de datos.")

    def mostrar_info(self):
        return f"Fecha: {self.fecha}, Tipo: {self.tipo}, Cantidad: {self.cantidad} hectáreas, Temporada: {self.temporada}"


fecha = input("Ingrese la fecha de la cosecha (D/M/A): ")
tipo = input("Ingrese el tipo de cosecha de las disponibles (azucar, cafe): ").strip().lower()
cantidad = int(input("Ingrese las hectáreas cosechadas (1 a 30): "))
temporada = input("Ingrese si está en temporada de lluvia o seca: ").strip().lower()

Cosecha.agregar_cosecha(fecha, tipo, cantidad, temporada)

if tipo == "azucar" and 1 <= cantidad <= 5 and temporada == "lluvia":
    print("""
          Consejo: Aprovecha la fertilización orgánica o biológica, como compost o biofertilizantes. Esto ayuda a mejorar la estructura del suelo y a aumentar la resiliencia de la caña frente a enfermedades comunes en la temporada lluviosa.

          Consejo: Utiliza herramientas manuales (como machetes o azadas) o pequeñas máquinas como desmalezadoras para mantener la maleza bajo control. Esto es especialmente importante en la temporada de lluvias, cuando la maleza crece rápidamente.

          Consejo: Siembra la caña de azúcar en surcos elevados, lo cual mejora el drenaje y reduce el riesgo de inundaciones. Esto ayuda a asegurar que el exceso de agua se drene más rápidamente.
          """)
elif tipo == "azucar" and 6 >= cantidad <= 30 and temporada == "lluvia":
    print("""
          Consejo: Invertir en maquinaria de control de maleza mecanizado o sistemas de riego por goteo. Esto permitirá que el riego sea más eficiente y controlado, y el control de maleza sea más rápido y menos costoso.

          Consejo: Utiliza fertilización de liberación controlada y, si es posible, sistemas de fertilización variable a través de drones o sensores de suelo. Esto asegura que cada sección del terreno reciba los nutrientes que necesita.

          Consejo: Realiza una cosecha escalonada en diferentes secciones del campo. Esto permite que la caña de azúcar no se dañe por lluvias inesperadas, y permite más tiempo para el secado y la recolección de la caña sin afectar la calidad.
          """)
elif tipo == "azucar" and 1 <= cantidad <= 5 and temporada == "seca":
    print("""
          Consejo: Instala un sistema de riego por goteo o riego por surcos para asegurar que cada planta reciba la cantidad adecuada de agua sin generar pérdidas. Si no tienes un sistema automatizado, asegúrate de realizar riego profundo y espaciado para incentivar las raíces profundas.

          Consejo: Aplica una capa de mulching orgánico (como paja o residuos vegetales) alrededor de la base de las plantas para reducir la evaporación. Esto ayudará a conservar la humedad del suelo y protegerá las raíces del calor excesivo.

          Consejo: Si vas a sembrar nuevamente o tienes la opción de renovar tus cultivos, selecciona variedades de caña de azúcar resistentes a la sequía o de ciclo más corto. Las variedades como Co 86032 o Pioneer 35-60 son conocidas por su tolerancia a la sequía y requieren menos agua.
          """)
elif tipo == "azucar" and 6 >= cantidad <= 30 and temporada == "seca":
    print("""
          Consejo: Utiliza un sistema de riego por goteo o aspersores de bajo consumo para asegurar que el agua llegue directamente a las raíces, minimizando el desperdicio por evaporación. Considera también el uso de sensores de humedad para controlar los niveles de agua en el suelo.

          Consejo: Incorpora compost o estiércol bien descompuesto en el suelo antes de la siembra, y aplica bioestimulantes para mejorar la estructura del suelo y su capacidad de retención de agua.

          Consejo: Aplica fertilización foliar con micronutrientes esenciales (como potasio, magnesio, y calcio) para ayudar a las plantas a superar el estrés y mantener su crecimiento. La fertilización foliar se absorbe rápidamente y es especialmente útil cuando el suelo está seco y no puede absorber los nutrientes de manera eficiente.
          """)
    

elif tipo == "cafe" and 1 <= cantidad <= 5 and temporada == "lluvia":
    print("""
          Consejo: La lluvia puede causar erosión en campos pequeños. Coloca barreras vegetales o muros de contención en las pendientes del terreno para reducir la pérdida de suelo y proteger las raíces del café.

          Consejo: Durante la temporada de lluvias, el aire se vuelve más húmedo. Es importante permitir que las plantas tengan buena circulación de aire para evitar enfermedades fúngicas, como la roya del café. Puedes podar algunas ramas o instalar estructuras de soporte para evitar el exceso de humedad en la planta.

          Consejo: Para evitar que las lluvias fuertes afecten la cosecha, usa mallas o coberturas plásticas sobre las plantas más vulnerables. Esto ayudará a proteger los granos de café de las lluvias torrenciales y mantendrá la calidad del grano.
          """)
elif tipo == "cafe" and 6 >= cantidad <= 30 and temporada == "lluvia":
    print("""
          Consejo: En terrenos grandes, el exceso de agua puede ser un problema. Instala un sistema de drenaje eficiente en los caminos entre las filas de plantas para evitar que el agua se acumule en las raíces del café.

          Consejo: Con grandes áreas de cultivo, es clave fomentar la biodiversidad plantando árboles de sombra y plantas asociadas. Esto no solo mejora la salud del suelo, sino que también crea un microclima más estable y reduce el impacto de las lluvias.

          Consejo: En áreas grandes, realiza la cosecha diferenciada en función de la madurez del café. Las lluvias pueden hacer que las frutas maduren a diferentes velocidades, por lo que cosechar por etapas asegura que el grano esté en el punto óptimo.
          """)    
elif tipo == "cafe" and 1 <= cantidad <= 5 and temporada == "seca":
    print("""
          Consejo: Con grandes superficies, instala una capa gruesa de mulching (como paja o compost) sobre el suelo. Esto conserva la humedad y evita la evaporación, protegiendo las raíces del calor.

          Consejo: En terrenos grandes, implementa un sistema de monitoreo para verificar el estrés térmico de las plantas. Sensores de temperatura o incluso observación visual (color de hojas) te pueden ayudar a ajustar el riego de forma precisa.

          Consejo: Si tienes espacio, planta cultivos de cobertura como trébol o alfalfa entre las hileras de café. Estos cultivos protegen el suelo de la erosión, mejoran
         """)
elif tipo == "cafe" and 6 >= cantidad <= 30 and temporada == "seca":
    print("""
          Consejo: En terrenos grandes y en temporada seca, asegúrate de implementar un sistema de riego eficiente.

          Consejo: Realiza podas ligeras para mejorar la aireación y reducir el estrés hídrico.
          
          Consejo: Mantén una cobertura vegetal o mulching para conservar la humedad del suelo y evitar erosión.
          """)

else:
    print("Cultivo no disponible o datos incorrectos.")


# Clases vs Objetos

## Objetivos de Aprendizaje

- ✅ Comprender el **concepto de clases y objetos** en programación.
- ✅ Aprender cómo las **clases definen plantillas** y los **objetos representan instancias reales** de esas plantillas.
- ✅ Reconocer cómo las **clases y los objetos se relacionan con conceptos del mundo real.**

## ¿Qué es una Clase?

Una **clase** es una **plantilla** o **modelo** para crear objetos. Define las propiedades (**atributos**) y los comportamientos (**métodos**) que tendrán los objetos. Sin embargo, una clase en sí misma **no es un objeto**, sino una estructura que describe cómo deben comportarse los objetos de ese tipo.

### Analogía del Mundo Real

Piensa en un **plano de una casa**. El plano define cómo debería verse la casa —cuántas habitaciones, puertas y ventanas tiene— pero el plano en sí mismo **no es una casa**. Es solo un plan.

Digamos que `Car` es una **clase** que define atributos (`brand`, `color`) y un comportamiento (el método `drive()`). **Todavía no es un coche real** —solo una descripción de uno.

---

## ¿Qué es un Objeto?

Un **objeto** es una **instancia de una clase**. Cuando se usa una clase para crear un objeto, este obtiene sus propios **valores reales** para los atributos y puede usar los métodos definidos en la clase.

### Analogía del Mundo Real

Una **casa específica construida a partir de un plano** es un objeto. Cada casa (objeto) sigue la misma estructura general (clase) pero tiene sus **propias características únicas** (color, dirección, propietario).

### Ejemplo en Programación

```python
my_car = Car("Toyota", "Red")  # Creando un objeto (instancia de Car)
print(my_car.drive())  # Salida: The Red Toyota is driving.
```

`my_car` es un **objeto**, un **coche real** basado en la clase `Car`.

---

## Diferencias Clave entre Clases y Objetos

| Característica | Clase | Objeto |
|----------------|-------|--------|
| Definición | Una plantilla o modelo | Una instancia real creada a partir de la clase |
| ¿Existe en Memoria? | No, solo es una definición | Sí, ocupa memoria cuando se crea |
| ¿Puede Almacenar Datos? | No, solo define atributos | Sí, tiene valores reales para los atributos |
| ¿Puede Realizar Acciones? | No, solo define métodos | Sí, puede ejecutar métodos |

---

## ¿Por qué usar Clases y Objetos?

**Reutilización de Código** — Define una clase una vez, crea muchos objetos a partir de ella.  
**Organización** — Ayuda a estructurar programas grandes agrupando datos y funciones relacionados.  
**Escalabilidad** — Facilita la modificación y extensión de la funcionalidad.

Al comprender las clases y los objetos, los programadores pueden **modelar entidades del mundo real de forma eficiente**, haciendo el código más **estructurado y reutilizable.**

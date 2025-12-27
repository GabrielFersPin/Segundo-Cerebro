---
cards-deck: Fundamentos DS
created: 2025-12-15 19:17
modified: 2025-12-27 02:22
status: 🌱 Semilla
tipo_nota: tecnica
asignatura: Fundamentos-DS
procesamiento: PROCESADO
prioridad: EXAMEN-LEJANO
tipo-captura: concepto
fecha-examen: ""
proxima-revision: 2026-01-03
complejidad: ⭐⭐
tiempo-estimado: 15 min
origen: Clase
urgente: false
---

# Regresión Logística

> [!abstract] Definición Rápida
> A pesar de su nombre "Regresión", es un algoritmo de **CLASIFICACIÓN**.
> Se usa para predecir la probabilidad de que algo sea Verdadero (1) o Falso (0).
> **Ejemplo**: ¿Este email es Spam? (Sí/No)

---

## 🧠 ¿Qué es y cómo funciona?

Imagina que quieres clasificar si un tumor es maligno (1) o benigno (0) según su tamaño.

* Si usaras **Regresión Lineal**, la línea recta podría darte valores como 1.5 o -0.2 (lo cual no tiene sentido para una probabilidad).
* La **Regresión Logística** "aplasta" esa línea para que siempre esté entre 0 y 1.

### La Función Sigmoide (La clave de todo) 📉

Es la función matemática que convierte cualquier número (infinito negativo a infinito positivo) en un valor entre 0 y 1.

$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

* Si $z$ es muy grande positivo $\to$ Probabilidad $\approx 1$
* Si $z$ es muy grande negativo $\to$ Probabilidad $\approx 0$
* Si $z = 0$ $\to$ Probabilidad $= 0.5$ (El punto de decisión)

---

## 🆚 Diferencias Clave

| Característica | Regresión Lineal | Regresión Logística |
| :--- | :--- | :--- |
| **Objetivo** | Predecir un número continuo (Ej: Precio de casa) | Predecir una etiqueta/clase (Ej: Gato o Perro) |
| **Salida** | $(-\infty, +\infty)$ | Probabilidad $[0, 1]$ |
| **Línea de ajuste** | Recta | Curva en forma de "S" (Sigmoide) |
| **Uso principal** | Predicción / Forecasting | Clasificación Binaria |

---

## 🎲 Concepto de Odds (Posibilidades)

Es otra forma de expresar probabilidad, muy usada en apuestas.
$$
Odds = \frac{P(\text{éxito})}{P(\text{fracaso})} = \frac{P}{1-P}
$$

**Ejemplo**:

* Probabilidad de ganar = 0.8
* Probabilidad de perder = 0.2
* $Odds = 0.8 / 0.2 = 4$
* Significa: "Es 4 veces más probable ganar que perder".

> [!tip] Log-Odds (Logit)
> Si aplicas el logaritmo a las Odds, obtienes una línea recta. De ahí viene la conexión con la regresión lineal.
> $\ln(\frac{P}{1-P}) = \beta_0 + \beta_1X$

---

## � Ejemplo en Python (Scikit-Learn)

```python
from sklearn.linear_model import LogisticRegression

# 1. Crear el modelo
modelo = LogisticRegression()

# 2. Entrenar (X = datos, y = etiquetas 0 o 1)
modelo.fit(X_train, y_train)

# 3. Predecir
prediccion = modelo.predict(X_new)         # Devuelve 0 o 1
probabilidad = modelo.predict_proba(X_new) # Devuelve [0.2, 0.8]
```

---

## 🎴 Flashcards para Examen

¿La Regresión Logística es para regresión o clasificación?::Clasificación (a pesar del nombre).

¿Qué función fuerza la salida a estar entre 0 y 1?::La función Sigmoide.

¿Cuál es el umbral (threshold) por defecto para decidir 0 o 1?::0.5

---

## 🔗 Referencias

- [[Regresión Lineal]] (Su hermana para variables continuas)
* [[Matriz de Confusión]] (Cómo evaluamos si el modelo funciona)

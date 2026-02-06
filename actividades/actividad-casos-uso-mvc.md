# 🎯 ACTIVIDAD PRÁCTICA: Casos de Uso y Arquitectura MVC

## 📋 Información General

**Título:** Diseño de Sistema con Casos de Uso y Arquitectura MVC  
**Nivel:** Principiante  
**Duración estimada:** 3-4 horas  
**Modalidad:** Individual  
**Entregables:** Diagrama de Casos de Uso + Documento de Análisis + Diseño MVC

---

## 🎓 Objetivos de Aprendizaje

Al completar esta actividad, serás capaz de:
- ✅ Comprender los elementos técnicos básicos de un sistema software
- ✅ Identificar actores y funcionalidades de un sistema
- ✅ Crear diagramas de casos de uso en UML
- ✅ Aplicar el patrón de diseño Modelo-Vista-Controlador (MVC)
- ✅ Relacionar casos de uso con componentes del sistema

---

## 📚 Conocimientos Previos Necesarios

Antes de empezar, asegúrate de haber estudiado:
- [ ] Conceptos básicos de UML
- [ ] Qué es un sistema de software
- [ ] Diferencia entre usuario y sistema

**Si necesitas repasar:** Ver recursos al final de este documento.

---

## 🛠️ Herramientas Necesarias

### Software a instalar:

1. **Herramienta de diagramas UML** (elige una):
   - **draw.io** (https://app.diagrams.net/) - ✅ Recomendado, gratis, sin instalación
   - Lucidchart (versión gratuita)
   - Visual Paradigm Community Edition

2. **Editor de texto** (elige uno):
   - Microsoft Word / Google Docs
   - Notion
   - Markdown editor (Typora, VS Code)

3. **Papel y lápiz** (opcional):
   - Puedes hacer el diagrama a mano y tomar foto

---

## 🚀 PARTE 1: Nociones Técnicas Esenciales (60 minutos)

### Paso 1.1: Lee y Comprende los Conceptos

Lee cada concepto y responde las preguntas de reflexión:

---

#### 📊 **Concepto 1: ¿Qué es una Base de Datos?**

**Definición:**
> Una base de datos es un lugar organizado donde el sistema guarda información para usarla después.

**Analogía cotidiana:**
Imagina una libreta donde anotas:
- 📞 Contactos
- ✅ Tareas pendientes
- 💰 Gastos del mes

La diferencia es que una base de datos digital:
- ✓ Guarda miles de datos
- ✓ Los busca en milisegundos
- ✓ No se pierde aunque apagues la computadora

**Ejemplos en proyectos:**

| Tipo de Sistema | ¿Qué guardaría? |
|-----------------|-----------------|
| Sistema escolar | Estudiantes, materias, calificaciones |
| Tienda online | Productos, clientes, pedidos |
| App de tareas | Tareas, fechas, prioridades |
| Sistema médico | Pacientes, citas, recetas |

**🤔 Pregunta de reflexión:**
```
Piensa en una app que uses (WhatsApp, Instagram, Spotify).
¿Qué información crees que guarda en su base de datos?

Tu respuesta (escribe 3-5 ejemplos):
1. ___________________________________
2. ___________________________________
3. ___________________________________
```

---

#### 📄 **Concepto 2: ¿Qué es un archivo JSON?**

**Definición:**
> JSON es una forma sencilla de guardar información en texto, con una estructura clara y legible.

**Ejemplo visual:**
```json
{
  "usuario": "Ana García",
  "edad": 20,
  "carrera": "Ingeniería",
  "activo": true,
  "materias": ["UML", "Programación", "Bases de Datos"]
}
```

**¿Cuándo se usa JSON en lugar de base de datos?**

| Situación | ¿Usar JSON? | ¿Usar BD? |
|-----------|-------------|-----------|
| Guardar configuraciones del sistema | ✅ | ❌ |
| Almacenar 10,000 usuarios | ❌ | ✅ |
| Exportar datos para compartir | ✅ | ❌ |
| Sistema con búsquedas complejas | ❌ | ✅ |
| Guardar preferencias del usuario | ✅ | ❌ |

**🤔 Pregunta de reflexión:**
```
En tu proyecto, ¿qué información guardarías en JSON y qué en base de datos?

JSON (datos simples):
___________________________________

Base de Datos (datos complejos):
___________________________________
```

---

#### 🗄️ **Concepto 3: ¿Qué es SQLite?**

**Definición:**
> SQLite es una base de datos ligera que se integra directamente en tu programa, sin necesidad de servidor.

**Características:**
- ✓ **Ligera:** Un solo archivo `.db`
- ✓ **Sin servidor:** No necesitas instalar nada extra
- ✓ **Portátil:** Puedes copiar el archivo y llevarlo a otra computadora
- ✓ **Perfecta para:** Proyectos escolares, apps de escritorio, prototipos

**Comparación visual:**
```
┌─────────────────────────────────────────┐
│ SQLite (lo que usarás)                  │
├─────────────────────────────────────────┤
│ ✓ Todo en un archivo                    │
│ ✓ No necesita instalación               │
│ ✓ Ideal para aprender                   │
│ ✓ Proyectos pequeños/medianos           │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│ MySQL/PostgreSQL (bases más grandes)    │
├─────────────────────────────────────────┤
│ ✓ Necesita servidor                     │
│ ✓ Instalación compleja                  │
│ ✓ Para sistemas empresariales           │
│ ✓ Miles de usuarios simultáneos         │
└─────────────────────────────────────────┘
```

---

#### 🎨 **Concepto 4: ¿Qué es CustomTkinter?**

**Definición:**
> CustomTkinter es una librería de Python para crear interfaces gráficas modernas y atractivas.

**¿Qué puedes crear con CustomTkinter?**

| Elemento | Ejemplo de Uso |
|----------|----------------|
| 🪟 Ventanas | Pantalla principal del sistema |
| 🔘 Botones | "Guardar", "Cancelar", "Iniciar Sesión" |
| 📝 Formularios | Campos para nombre, email, contraseña |
| 📋 Listas | Mostrar productos, tareas, usuarios |
| 📊 Tablas | Visualizar datos organizados |
| 🎨 Menús | Navegación entre secciones |

**Ejemplo de código simple:**
```python
import customtkinter as ctk

# Crear ventana
app = ctk.CTk()
app.title("Mi Primera App")

# Crear botón
boton = ctk.CTkButton(app, text="Click aquí")
boton.pack()

# Mostrar ventana
app.mainloop()
```

**🤔 Pregunta de reflexión:**
```
Para tu proyecto, lista 3 ventanas que necesitarías:

1. Ventana de: ___________________________
   ¿Qué elementos tendría? (botones, campos, etc.)
   ___________________________________

2. Ventana de: ___________________________
   ¿Qué elementos tendría?
   ___________________________________

3. Ventana de: ___________________________
   ¿Qué elementos tendría?
   ___________________________________
```

---

#### 🏗️ **Concepto 5: Modelo Vista Controlador (MVC)**

**Definición:**
> MVC es una forma de organizar tu código en 3 partes separadas para que sea más fácil de mantener.

**Las 3 Capas Explicadas:**

```
┌─────────────────────────────────────────────────┐
│             👁️ VISTA (View)                     │
│  Lo que el usuario VE e INTERACTÚA              │
├─────────────────────────────────────────────────┤
│  • Ventanas                                     │
│  • Botones                                      │
│  • Formularios                                  │
│  • Mensajes                                     │
│                                                 │
│  Ejemplo: formulario_login.py                   │
└─────────────────────────────────────────────────┘
            ↕️ se comunica con
┌─────────────────────────────────────────────────┐
│         🎮 CONTROLADOR (Controller)             │
│  PROCESA las acciones del usuario               │
├─────────────────────────────────────────────────┤
│  • Recibe eventos (clicks)                      │
│  • Valida datos                                 │
│  • Coordina Vista y Modelo                      │
│  • Muestra mensajes de error                    │
│                                                 │
│  Ejemplo: controlador_login.py                  │
└─────────────────────────────────────────────────┘
            ↕️ se comunica con
┌─────────────────────────────────────────────────┐
│           💾 MODELO (Model)                     │
│  MANEJA los datos (guarda/obtiene)              │
├─────────────────────────────────────────────────┤
│  • Conecta con la base de datos                 │
│  • Guarda información                           │
│  • Obtiene información                          │
│  • Valida reglas de negocio                     │
│                                                 │
│  Ejemplo: modelo_usuario.py                     │
└─────────────────────────────────────────────────┘
```

**Ejemplo práctico: Sistema de Login**

**Flujo paso a paso:**

1. **VISTA:** Usuario escribe email y contraseña, da click en "Iniciar Sesión"

2. **CONTROLADOR:** 
   - Recibe el email y contraseña
   - Valida que no estén vacíos
   - Llama al Modelo para verificar

3. **MODELO:**
   - Busca en la base de datos si existe el usuario
   - Verifica si la contraseña es correcta
   - Devuelve resultado al Controlador

4. **CONTROLADOR:**
   - Si es correcto: indica a la Vista que abra la ventana principal
   - Si es incorrecto: indica a la Vista que muestre error

5. **VISTA:** Muestra la ventana principal o mensaje de error

**🤔 Ejercicio de identificación:**
```
Imagina que tienes un botón "Guardar Tarea" en tu sistema.

Identifica qué parte hace qué:

VISTA hace:
___________________________________
(Ejemplo: Muestra el botón y el formulario)

CONTROLADOR hace:
___________________________________
(Ejemplo: Recibe el click, valida que los campos no estén vacíos)

MODELO hace:
___________________________________
(Ejemplo: Guarda la tarea en la base de datos)
```

---

#### 📦 **Concepto 6: PyInstaller**

**Definición:**
> PyInstaller convierte tu programa de Python en un archivo ejecutable (.exe) que cualquiera puede usar sin tener Python instalado.

**¿Por qué es útil?**

| Sin PyInstaller | Con PyInstaller |
|-----------------|-----------------|
| ❌ Necesitas tener Python instalado | ✅ Solo doble click en el .exe |
| ❌ Necesitas instalar librerías | ✅ Todo incluido en un archivo |
| ❌ Solo programadores pueden usarlo | ✅ Cualquier persona puede usarlo |
| ❌ Difícil de compartir | ✅ Fácil de distribuir |

**Comando básico:**
```bash
pyinstaller --onefile --windowed mi_programa.py
```

Esto genera: `mi_programa.exe` (Windows) o `mi_programa.app` (Mac)

---

### Paso 1.2: Completa tu Documento de Análisis

Crea un documento llamado `analisis_tecnico.pdf` o `.docx` y responde:

```
ANÁLISIS TÉCNICO DE MI PROYECTO
================================

1. DESCRIPCIÓN DEL PROYECTO
   Describe brevemente tu idea de sistema (3-5 líneas):
   
   _______________________________________________
   _______________________________________________
   _______________________________________________

2. ALMACENAMIENTO DE DATOS
   
   a) ¿Qué información necesitará guardar tu sistema?
      (Lista al menos 5 tipos de datos)
      
      1. _______________________________________________
      2. _______________________________________________
      3. _______________________________________________
      4. _______________________________________________
      5. _______________________________________________
   
   b) ¿Usarás Base de Datos (SQLite) o JSON? ¿Por qué?
   
      Decisión: _______________________
      
      Justificación:
      _______________________________________________
      _______________________________________________

3. INTERFAZ GRÁFICA
   
   a) ¿Tendrá ventanas o formularios?
      
      [ ] Sí    [ ] No
   
   b) Lista las 3 ventanas principales:
      
      1. _______________________________________________
      2. _______________________________________________
      3. _______________________________________________

4. USUARIOS DEL SISTEMA
   
   ¿Quién usará el sistema? (ejemplo: estudiantes, administrador, clientes)
   
   1. _______________________________________________
   2. _______________________________________________
   3. _______________________________________________

5. ARQUITECTURA MVC
   
   Basándote en lo que aprendiste sobre MVC, identifica:
   
   MODELO (Manejo de datos):
   ¿Qué información se guardará/obtendrá?
   
   _______________________________________________
   _______________________________________________
   
   VISTA (Interfaz gráfica):
   ¿Qué ventanas tendrá el sistema?
   
   _______________________________________________
   _______________________________________________
   
   CONTROLADOR (Lógica de negocio):
   ¿Qué acciones procesará? (validaciones, cálculos, etc.)
   
   _______________________________________________
   _______________________________________________
```

**📌 Checkpoint 1:** Antes de continuar, asegúrate de haber completado todo el documento de análisis.

---

## 🧩 PARTE 2: Diagramas de Caso de Uso (90-120 minutos)

### Paso 2.1: Comprende los Conceptos de Casos de Uso

#### 📘 ¿Qué es un Diagrama de Casos de Uso?

**Definición:**
> Un diagrama de casos de uso muestra QUÉ puede hacer el sistema y QUIÉN interactúa con él.

**❗ Importante:**
- ✅ Muestra **funcionalidades** (qué hace el sistema)
- ❌ NO muestra **cómo se programa**

**Ejemplo:**
```
Sistema de Netflix

¿Qué muestra el diagrama de casos de uso?
✅ Buscar película
✅ Reproducir contenido
✅ Crear perfil

¿Qué NO muestra?
❌ Cómo se conecta a la base de datos
❌ En qué lenguaje está programado
❌ Cómo funciona el algoritmo de recomendaciones
```

---

#### 🎭 ¿Qué es un Actor?

**Definición:**
> Un actor es alguien o algo EXTERNO que interactúa con el sistema.

**Tipos de actores:**

| Tipo | Ejemplo |
|------|---------|
| 👤 Persona | Usuario, Administrador, Cliente, Estudiante |
| 🤖 Sistema externo | API de pagos, Servidor de emails, GPS |
| ⏰ Tiempo | Sistema que ejecuta tareas programadas |

**¿Cómo identificar actores?**

Hazte estas preguntas:
1. ¿Quién **usa** el sistema?
2. ¿Quién **administra** el sistema?
3. ¿Qué sistemas **externos** se conectan?

**Ejemplo: Sistema de Biblioteca**
- 👨‍🎓 Estudiante (usa el sistema para buscar libros)
- 👨‍💼 Bibliotecario (administra préstamos)
- 📧 Sistema de Email (envía notificaciones)

**❌ Errores comunes:**
- NO es actor: "Base de datos" (es parte interna del sistema)
- NO es actor: "Botón de login" (es parte de la interfaz)
- SÍ es actor: "Usuario" (interactúa desde fuera)

---

#### 🎯 ¿Qué es un Caso de Uso?

**Definición:**
> Un caso de uso es una **acción importante** que el sistema puede realizar.

**Formato recomendado:**
```
VERBO + OBJETO

✅ Correcto:
- Registrar usuario
- Buscar producto
- Generar reporte
- Iniciar sesión

❌ Incorrecto:
- Usuario (no es acción)
- Base de datos (no es acción)
- Click en botón (muy específico)
```

**¿Cómo identificar casos de uso?**

Pregúntate:
1. ¿Qué **acciones principales** puede hacer cada actor?
2. ¿Qué **objetivos** quiere lograr el usuario?
3. ¿Qué **funcionalidades** son importantes?

**Ejemplo: Sistema de Tareas Escolares**

Actor: **Estudiante**

Casos de uso:
- ✅ Crear tarea
- ✅ Marcar tarea como completada
- ✅ Consultar tareas pendientes
- ✅ Eliminar tarea
- ✅ Editar tarea

**⚠️ Nivel de detalle correcto:**
- ✅ "Registrar usuario" (correcto: acción completa)
- ❌ "Validar email" (muy detallado: es parte de registrar)
- ❌ "Click en botón registrar" (muy específico: es implementación)

---

### Paso 2.2: Aprende a Dibujar Casos de Uso

#### Simbología UML para Casos de Uso

```
┌─────────────────────────────────────────────┐
│  ELEMENTOS DEL DIAGRAMA                     │
├─────────────────────────────────────────────┤
│                                             │
│  1. ACTOR (muñeco de palitos)               │
│        👤                                    │
│      Usuario                                │
│                                             │
│  2. CASO DE USO (óvalo)                     │
│      ┌──────────────┐                       │
│      │ Iniciar      │                       │
│      │ sesión       │                       │
│      └──────────────┘                       │
│                                             │
│  3. SISTEMA (rectángulo grande)             │
│      ┌──────────────────────┐               │
│      │  Sistema de Tareas   │               │
│      │                      │               │
│      │  (casos de uso aquí) │               │
│      └──────────────────────┘               │
│                                             │
│  4. RELACIÓN (línea simple)                 │
│      👤 ────────── (Caso de Uso)            │
│                                             │
└─────────────────────────────────────────────┘
```

---

#### Ejemplo Completo Paso a Paso

**Sistema:** Aplicación de Tareas Académicas

**Paso 1: Identificar el actor principal**
```
Actor: Estudiante
```

**Paso 2: Identificar casos de uso**
```
1. Crear tarea
2. Marcar tarea como completada
3. Consultar tareas pendientes
```

**Paso 3: Dibujar en draw.io**

Instrucciones detalladas:

1. **Abrir draw.io:**
   - Ve a https://app.diagrams.net/
   - Create New Diagram
   - Blank Diagram

2. **Dibujar el rectángulo del sistema:**
   - Busca en la barra izquierda: "Rectangle"
   - Arrastra al canvas
   - Hazlo grande (aproximadamente 600x400 px)
   - Doble click → Escribe: "Sistema de Tareas"

3. **Agregar el actor:**
   - Busca en UML: "Actor" (muñeco)
   - Arrastra FUERA del rectángulo (a la izquierda)
   - Doble click debajo → Escribe: "Estudiante"

4. **Agregar casos de uso:**
   - Busca en UML: "Use Case" (óvalo)
   - Arrastra 3 óvalos DENTRO del rectángulo del sistema
   - Escribe en cada uno:
     - "Crear tarea"
     - "Marcar completada"
     - "Consultar tareas"

5. **Conectar con líneas:**
   - Busca: "Line" o "Connector"
   - Dibuja línea desde el Actor hasta cada Caso de Uso
   - Las líneas deben ser simples (sin flechas)

**Resultado visual:**

```
                  ┌─────────────────────────────────┐
                  │  Sistema de Tareas Académicas   │
                  │                                 │
    👤            │    ┌──────────────┐             │
  Estudiante ─────│────│ Crear tarea  │             │
     │            │    └──────────────┘             │
     │            │                                 │
     │            │    ┌──────────────┐             │
     └────────────│────│   Marcar     │             │
     │            │    │  completada  │             │
     │            │    └──────────────┘             │
     │            │                                 │
     │            │    ┌──────────────┐             │
     └────────────│────│  Consultar   │             │
                  │    │   tareas     │             │
                  │    └──────────────┘             │
                  │                                 │
                  └─────────────────────────────────┘
```

---

### Paso 2.3: Crea TU Diagrama de Casos de Uso

**Instrucciones:**

#### Tarea 1: Identifica Actores y Casos de Uso

Completa esta tabla para TU proyecto:

```
MI PROYECTO: _________________________________

ACTORES (al menos 1, máximo 3):
┌────────────────────────────────────────────┐
│ Actor 1: _______________________________   │
│ ¿Qué hace? ____________________________    │
│                                            │
│ Actor 2: _______________________________   │
│ ¿Qué hace? ____________________________    │
│                                            │
│ Actor 3: _______________________________   │
│ ¿Qué hace? ____________________________    │
└────────────────────────────────────────────┘

CASOS DE USO (mínimo 3, máximo 6):
┌────────────────────────────────────────────┐
│ 1. ______________________________________  │
│    Actor que lo ejecuta: _______________   │
│                                            │
│ 2. ______________________________________  │
│    Actor que lo ejecuta: _______________   │
│                                            │
│ 3. ______________________________________  │
│    Actor que lo ejecuta: _______________   │
│                                            │
│ 4. ______________________________________  │
│    Actor que lo ejecuta: _______________   │
│                                            │
│ 5. ______________________________________  │
│    Actor que lo ejecuta: _______________   │
│                                            │
│ 6. ______________________________________  │
│    Actor que lo ejecuta: _______________   │
└────────────────────────────────────────────┘
```

**✅ Checklist de validación:**
- [ ] Los casos de uso están escritos con VERBO + OBJETO
- [ ] Los casos de uso son acciones que el USUARIO VE (no código interno)
- [ ] Cada actor tiene al menos un caso de uso asociado
- [ ] No incluí elementos técnicos como "Base de datos" como actores

---

#### Tarea 2: Dibuja el Diagrama

**Opción A: Digital (Recomendado)**

1. Abre draw.io
2. Sigue los pasos del ejemplo anterior
3. Guarda como: `casos_uso_[TuApellido].png`

**Opción B: A mano**

1. Dibuja en una hoja blanca
2. Usa regla para el rectángulo del sistema
3. Toma foto clara y bien iluminada
4. Guarda como: `casos_uso_[TuApellido].jpg`

**⚠️ Requisitos mínimos:**
- [ ] Rectángulo del sistema con título
- [ ] Al menos 1 actor (muñeco)
- [ ] Al menos 3 casos de uso (óvalos)
- [ ] Líneas conectando actor con casos de uso
- [ ] Nombres claros y legibles

---

### Paso 2.4: Relaciona Casos de Uso con Ventanas

Para cada caso de uso que identificaste, indica qué ventana del sistema lo ejecutaría:

```
RELACIÓN CASO DE USO ↔ VENTANA/PANTALLA
=========================================

Caso de Uso 1: _____________________________
┌────────────────────────────────────────────┐
│ Ventana/Pantalla: ______________________   │
│                                            │
│ Elementos de la interfaz:                  │
│ - ______________________________________   │
│ - ______________________________________   │
│ - ______________________________________   │
│                                            │
│ ¿Qué datos se guardan?                     │
│ ________________________________________   │
│ ________________________________________   │
└────────────────────────────────────────────┘

Caso de Uso 2: _____________________________
┌────────────────────────────────────────────┐
│ Ventana/Pantalla: ______________________   │
│                                            │
│ Elementos de la interfaz:                  │
│ - ______________________________________   │
│ - ______________________________________   │
│ - ______________________________________   │
│                                            │
│ ¿Qué datos se guardan?                     │
│ ________________________________________   │
│ ________________________________________   │
└────────────────────────────────────────────┘

Caso de Uso 3: _____________________________
┌────────────────────────────────────────────┐
│ Ventana/Pantalla: ______________________   │
│                                            │
│ Elementos de la interfaz:                  │
│ - ______________________________________   │
│ - ______________________________________   │
│ - ______________________________________   │
│                                            │
│ ¿Qué datos se guardan?                     │
│ ________________________________________   │
│ ________________________________________   │
└────────────────────────────────────────────┘
```

**Ejemplo de respuesta:**

```
Caso de Uso 1: Crear tarea

┌────────────────────────────────────────────┐
│ Ventana/Pantalla: Formulario de nueva tarea│
│                                            │
│ Elementos de la interfaz:                  │
│ - Campo de texto: Título de la tarea       │
│ - Campo de texto: Descripción              │
│ - Selector de fecha: Fecha límite          │
│ - Botón: "Guardar tarea"                   │
│ - Botón: "Cancelar"                        │
│                                            │
│ ¿Qué datos se guardan?                     │
│ - Título de la tarea                       │
│ - Descripción                              │
│ - Fecha límite                             │
│ - Estado: "Pendiente" (por defecto)        │
└────────────────────────────────────────────┘
```

---

## 📤 Entregables

Debes entregar en un archivo ZIP llamado `ApellidoNombre_CasosDeUso.zip` que contenga:

### 1. Documento de Análisis Técnico (obligatorio)
- **Archivo:** `analisis_tecnico.pdf` o `.docx`
- **Contenido:**
  - Descripción del proyecto
  - Análisis de almacenamiento (BD vs JSON)
  - Ventanas del sistema
  - Usuarios
  - Identificación MVC

### 2. Diagrama de Casos de Uso (obligatorio)
- **Archivo:** `casos_uso_[TuApellido].png` o `.jpg`
- **Contenido:**
  - Rectángulo del sistema
  - Mínimo 1 actor
  - Mínimo 3 casos de uso
  - Relaciones correctamente dibujadas

### 3. Tabla de Actores y Casos de Uso (obligatorio)
- **Archivo:** `tabla_casos_uso.pdf` o `.docx`
- **Contenido:**
  - Lista completa de actores
  - Lista completa de casos de uso
  - Actor responsable de cada caso de uso

### 4. Relación Casos de Uso ↔ Ventanas (obligatorio)
- **Archivo:** `relacion_ventanas.pdf` o `.docx`
- **Contenido:**
  - Para cada caso de uso: ventana correspondiente
  - Elementos de interfaz
  - Datos que se guardan

### 5. Video Explicativo (opcional - puntos extra)
- **Duración:** 3-5 minutos
- **Contenido:**
  - Explica tu proyecto
  - Muestra el diagrama
  - Explica cada caso de uso
  - Relaciona con las ventanas

---
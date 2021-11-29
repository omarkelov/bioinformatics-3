# Визуализация структуры белка

Программа: [OpenStructure](https://openstructure.org/).

Использованная структура: [7RUT](https://www.rcsb.org/structure/7rut).

# Способ визуализации

Для визуализации использовались скрипты на языке Python (блок в нижнем правом углу):

![Скрипты на языке Python](/pictures/10.png)

# Типы визуализации

## Wireframe

<details>
  <summary>Script</summary>

  ```python
scene.SetBackground(gfx.Color(0.1, 0.1, 0.1))
eh=io.LoadPDB("./examples/demos/data/7rut.pdb")
sdh_go=gfx.Entity("SDH", eh)
scene.Add(sdh_go)
scene.CenterOn(sdh_go)
sdh_go.SetColor(gfx.WHITE)
  ```
</details>

![Wireframe](/pictures/0.png)

## Backbone

<details>
  <summary>Script</summary>

  ```python
scene.SetBackground(gfx.Color(0.1, 0.1, 0.1))
eh=io.LoadPDB("./examples/demos/data/7rut.pdb")
sdh_go=gfx.Entity("SDH", eh)
scene.Add(sdh_go)
scene.CenterOn(sdh_go)
sdh_go.SetColor(gfx.WHITE)
  ```
</details>

![Backbone](/pictures/1.png)

## Ribbons

<details>
  <summary>Script</summary>

  ```python
scene.SetBackground(gfx.Color(0.1, 0.1, 0.1))
eh=io.LoadPDB("./examples/demos/data/7rut.pdb")
sdh_go=gfx.Entity("SDH", eh)
scene.Add(sdh_go)
scene.CenterOn(sdh_go)
sdh_go.SetRenderMode(gfx.RenderMode.HSC)
sdh_go.SetColor(gfx.Color(0.5, 0.5, 0.5), '')
sdh_go.SetColor(gfx.Color(0,1,0),"rtype=H")
sdh_go.SetDetailColor(gfx.Color(0.7,1.0,0.8),"rtype=H")
sdh_go.SetColor(gfx.Color(1,0,0),"rtype=E")
sdh_go.SetDetailColor(gfx.Color(1.0,0.8,0.2),"rtype=E")
  ```
</details>

![Ribbons](/pictures/8.png)

## CPK

<details>
  <summary>Script</summary>

  ```pythonscene.SetBackground(gfx.Color(0.1, 0.1, 0.1))
eh=io.LoadPDB("./examples/demos/data/7rut.pdb")
sdh_go=gfx.Entity("SDH", eh)
scene.Add(sdh_go)
scene.CenterOn(sdh_go)
sdh_go.SetRenderMode(gfx.CPK)
sdh_go.GetOptions(gfx.CPK).SetSphereDetail(4)
  ```
</details>

![CPK](/pictures/2.png)

## Tube

<details>
  <summary>Script</summary>

  ```pythonscene.SetBackground(gfx.Color(0.1, 0.1, 0.1))
scene.SetBackground(gfx.Color(0.5, 0.5, 0.5))
eh=io.LoadPDB("./examples/demos/data/7rut.pdb")
sdh_go=gfx.Entity("SDH", eh)
scene.Add(sdh_go)
scene.CenterOn(sdh_go)
sdh_go.SetRenderMode(gfx.TUBE)
sdh_go.tube_options.SetTubeRadius(0.8)
sdh_go.ColorBy("abfac",gfx.BLUE,gfx.RED)
sdh_go.RadiusBy("abfac",0.8,2.2)
  ```
</details>

![Tube](/pictures/4.png)

## Sline

<details>
  <summary>Script</summary>

  ```pythonscene.SetBackground(gfx.Color(0.1, 0.1, 0.1))
scene.SetBackground(gfx.Color(0.1, 0.1, 0.1))
eh=io.LoadPDB("./examples/demos/data/7rut.pdb")
sdh_go=gfx.Entity("SDH", eh)
scene.Add(sdh_go)
scene.CenterOn(sdh_go)
sdh_go.SetRenderMode(gfx.SLINE)
sdh_go.SetColor(gfx.YELLOW)
  ```
</details>

![Sline](/pictures/5.png)

## Trace

<details>
  <summary>Script</summary>

  ```pythonscene.SetBackground(gfx.Color(0.1, 0.1, 0.1))
scene.SetBackground(gfx.Color(0.1, 0.1, 0.1))
eh=io.LoadPDB("./examples/demos/data/7rut.pdb")
sdh_go=gfx.Entity("SDH", eh)
scene.Add(sdh_go)
scene.CenterOn(sdh_go)
sdh_go.SetRenderMode(gfx.TRACE)
  ```
</details>

![Trace](/pictures/6.png)

## Domains

<details>
  <summary>Script</summary>

  ```pythonscene.SetBackground(gfx.Color(0.1, 0.1, 0.1))
scene.SetBackground(gfx.Color(0.2, 0.2, 0.2))

eh=io.LoadPDB("./examples/demos/data/7rut.pdb")

sdh_go_d=gfx.Entity("SDH_D", eh.Select("cname=D"))
sdh_go_e=gfx.Entity("SDH_E", eh.Select("cname=E"))
scene.Add(sdh_go_d)
scene.Add(sdh_go_e)

sdh_go_d.SetColor(gfx.GREEN)
sdh_go_e.SetColor(gfx.RED)
sdh_go_d.SetRenderMode(gfx.CPK)
sdh_go_e.SetRenderMode(gfx.CPK)
sdh_go_d.GetOptions(gfx.CPK).SetSphereDetail(4)
sdh_go_e.GetOptions(gfx.CPK).SetSphereDetail(4)

scene.CenterOn(sdh_go_d)
  ```
</details>

![Domains](/pictures/9.png)

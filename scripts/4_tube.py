scene.SetBackground(gfx.Color(0.5, 0.5, 0.5))
eh=io.LoadPDB("./examples/demos/data/7rut.pdb")
sdh_go=gfx.Entity("SDH", eh)
scene.Add(sdh_go)
scene.CenterOn(sdh_go)
sdh_go.SetRenderMode(gfx.TUBE)
sdh_go.tube_options.SetTubeRadius(0.8)
sdh_go.ColorBy("abfac",gfx.BLUE,gfx.RED)
sdh_go.RadiusBy("abfac",0.8,2.2)


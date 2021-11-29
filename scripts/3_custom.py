scene.SetBackground(gfx.Color(0.1, 0.1, 0.1))
eh=io.LoadPDB("./examples/demos/data/7rut.pdb")
sdh_go=gfx.Entity("SDH", eh)
scene.Add(sdh_go)
scene.CenterOn(sdh_go)
sdh_go.SetRenderMode(gfx.CUSTOM)


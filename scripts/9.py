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


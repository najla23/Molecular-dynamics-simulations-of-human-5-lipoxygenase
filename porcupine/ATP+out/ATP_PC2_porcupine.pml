load ATP_PC2_extreme.pdb, pc2

split_states pc2
delete pc2

hide everything
show cartoon, pc2_0001
color gray80, pc2_0001

python
from pymol import cmd

start = "pc2_0001 and name CA"
end   = "pc2_0002 and name CA"

model1 = cmd.get_model(start)
model2 = cmd.get_model(end)

for i, (a1, a2) in enumerate(zip(model1.atom, model2.atom)):
    x1, y1, z1 = a1.coord
    x2, y2, z2 = a2.coord

    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1

    scale = 2.5

    cmd.pseudoatom(object="arrow_start_%d" % i, pos=[x1, y1, z1])
    cmd.pseudoatom(object="arrow_end_%d" % i, pos=[x1 + scale*dx, y1 + scale*dy, z1 + scale*dz])

    cmd.distance(
        name="arrow_%d" % i,
        selection1="arrow_start_%d" % i,
        selection2="arrow_end_%d" % i
    )

cmd.hide("labels")
cmd.hide("spheres", "arrow_start_*")
cmd.hide("spheres", "arrow_end_*")
cmd.set("dash_gap", 0.0)
cmd.set("dash_width", 3.0)
cmd.set("dash_color", "red")
python end

bg_color white
orient
zoom

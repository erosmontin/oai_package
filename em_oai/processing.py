import pynico_eros_montin.pynico as pn
import pyable_eros_montin.imaginable as ima




def fixrois(dess_file,label_file,output_label_file):
    dess=ima.Imaginable(dess_file)
    labelmap=ima.Imaginable(label_file)
    labelmap.setImageDirection(dess.getImageDirection())
    labelmap.setImageSpacing(dess.getImageSpacing())
    labelmap.setImageOrigin(dess.getImageOrigin())
    labelmap.writeImageAs(output_label_file)

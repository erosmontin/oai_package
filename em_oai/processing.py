import pynico_eros_montin.pynico as pn
import pyable_eros_montin.imaginable as ima



# dess segmentation is performed voxel wise.
# therefore we need to fix the roi files to have the same image direction, spacing and origin as the dess file
# this function does that
# dess_file: the dess file
# label_file: the roi file
# output_label_file: the output roi file

def fixrois(dess_file,label_file,output_label_file):
    dess=ima.Imaginable(dess_file)
    labelmap=ima.Imaginable(label_file)
    labelmap.setImageDirection(dess.getImageDirection())
    labelmap.setImageSpacing(dess.getImageSpacing())
    labelmap.setImageOrigin(dess.getImageOrigin())
    labelmap.writeImageAs(output_label_file)

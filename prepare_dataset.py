import one_time_rgb_normalize
import one_time_convert_hsv
import one_time_convert_hsv_xy
import one_time_convert_XYZ
import one_time_convert_xyY
import one_time_convert_cielab


def process():
    rgb = f"data_rgb.csv"
    hsv = f"data_hsv.csv"
    hsv_xy = f"data_hsv_xy.csv"
    XYZ_original = f"data_XYZ_original.csv"
    XYZ = f"data_XYZ.csv"
    xyY_original = f"data_xyY_original.csv"
    xyY = f"data_xyY.csv"
    cielab_original = f"data_cielab_original.csv"
    cielab = f"data_cielab.csv"

    one_time_convert_hsv.process(rgb, hsv)
    one_time_convert_hsv_xy.process(hsv, hsv_xy)
    one_time_convert_XYZ.process(rgb, XYZ_original, XYZ)
    one_time_convert_xyY.process(XYZ_original, xyY_original, xyY)
    one_time_convert_cielab.process(XYZ_original, cielab_original, cielab)


if __name__ == "__main__":
    one_time_rgb_normalize.process()
    process()
    print("All done")
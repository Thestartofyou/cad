import ezdxf

def create_cabinet_dxf(filename):
    doc = ezdxf.new()
    msp = doc.modelspace()

    # Define cabinet dimensions
    width = 100
    height = 200
    depth = 50

    # Draw cabinet outline
    msp.add_lwpolyline([(0, 0), (width, 0), (width, depth), (0, depth), (0, 0)], dxfattribs={'color': 7})

    # Draw shelves
    shelf_thickness = 10
    num_shelves = 2
    shelf_gap = (height - (num_shelves * shelf_thickness)) / (num_shelves + 1)
    for i in range(num_shelves):
        y = shelf_gap * (i + 1) + i * shelf_thickness
        msp.add_lwpolyline([(0, y), (width, y)], dxfattribs={'color': 7})

    # Save DXF file
    doc.saveas(filename)

if __name__ == "__main__":
    create_cabinet_dxf("cabinet.dxf")


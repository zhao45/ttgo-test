from PIL import Image
import os

def image_to_hex_array(image_path):
    img = Image.open(image_path)
    width, height = img.size
    pixel_values = list(img.getdata())
    hex_array = []
    
    for i in range(0, len(pixel_values), width):
        hex_row = []
        for j in range(width):
            pixel = pixel_values[i + j]
            hex_value = f"0x{pixel[0]:02X}{pixel[1]:02X}{pixel[2]:02X}"
            hex_row.append(hex_value)
        hex_array.append(hex_row)
    
    return hex_array

def generate_c_array(image_folder, output_file):
    files = os.listdir(image_folder)
    with open(output_file, "w") as f:
        for file in files:
            if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
                image_path = os.path.join(image_folder, file)
                hex_array = image_to_hex_array(image_path)
                f.write(f"const unsigned short PROGMEM {os.path.splitext(file)[0]}[] = {{\n")
                for row in hex_array:
                    f.write("    " + ", ".join(row) + ",\n")
                f.write("};\n\n")

# 示例用法：将当前文件夹下的所有图片转换成C语言数组形式，并输出到文件
if __name__ == "__main__":
    image_folder = "."  # 可以修改为包含图片的文件夹路径
    output_file = "image_arrays.c"  # 输出文件名，可以根据需要修改
    generate_c_array(image_folder, output_file)
    print(f"生成的C语言数组形式已保存到文件 {output_file}")

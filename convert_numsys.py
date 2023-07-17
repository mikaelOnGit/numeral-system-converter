import argparse
import sys

def DecToBin(dec_input, bin_output):
    while dec_input > 0:
        remainder = dec_input % 2 #remainder
        dec_input = dec_input // 2 #quotient
        bin_ouput.insert(0, str(remainder))
    print("Binary: " + "".join(bin_output))
    return bin_output

def BinToDec(bin_input, dec_output):
    bin_input = list(bin_input)
    e = 0
    for i in reversed(bin_input):
        dec_output += (int(i) * (2 ** e))
        e += 1
    print("Decimal: " + str(dec_output))
    return dec_output

def DecToHex(dec_input, hex_output):
    while dec_input > 0:
        remainder = dec_input % 16 #remainder
        dec_input = dec_input // 16 #quotient
        if remainder >= 10:
            if remainder == 10:
                hex_output.insert(0, "A")
            elif remainder == 11:
                hex_output.insert(0, "B")
            elif remainder == 12:
                hex_output.insert(0, "C")
            elif remainder == 13:
                hex_output.insert(0, "D")
            elif remainder == 14:
                hex_output.insert(0, "E")
            elif remainder == 15:
                hex_output.insert(0, "F")
        else:
            hex_output.insert(0, str(remainder))
    print("Hexadecimal: " + "".join(hex_output))
    return hex_output

def HexToDec(hex_input, dec_output):
    hex_input = list(hex_input)
    e = 0
    for i in reversed(hex_input):
        if i > 9:
            if i == "A" or i == "a":
                i = 10
            elif i == "B" or i == "b":
                i = 11
            elif i == "C" or i == "c":
                i = 12
            elif i == "D" or i == "d":
                i = 13
            elif i == "E" or i == "e":
                i = 14
            elif i == "F" or i == "f":
                i = 16
        dec_output += (int(i) * (16 ** e))
        e += 1
    print("Decimal: " + str(dec_output))
    return dec_output

def DecToOct(dec_input, oct_output):
    while dec_input > 0:
        remainder = dec_input % 8 #remainder
        dec_input = dec_input // 8 #quotient
        oct_output.insert(0, str(remainder))
    print("Octal: " + "".join(oct_output))
    return oct_output

def OctToDec(oct_input, dec_output):
    oct_input = list(oct_input)
    e = 0
    for i in reversed(oct_input):
        dec_output += (int(i) * (8 ** e))
        e += 1
    print("Decimal: " + str(dec_output))
    return dec_output

def TypeMatch(input_sys, value):
    if input_sys == "dec":
        try:
            int(value, 10)
            return True
        except ValueError:
            return False
    elif input_sys == "bin":
        try:
            int(value, 2)
            return True
        except ValueError:
            return False
    elif input_sys == "hex":
        try:
            int(value, 16)
            return True
        except ValueError:
            return False
    elif input_sys == "oct":
        try:
            int(value, 8)
            return True
        except ValueError:
            return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Basic positional numeral system converter",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("input",
                        choices = ["dec", "bin", "hex", "oct"],
                        help = "Input numeral system (format: dec, bin, hex, oct)")
    parser.add_argument("output",
                        choices = ["dec", "bin", "hex", "oct"],
                        help = "Output numeral system (format: dec, bin, hex, oct)")
    parser.add_argument("value",
                        type = str,
                        help = "Value to be converted")
    args = parser.parse_args()
    config = vars(args)
    print("This is your query: " + str(config))
    
    input_sys = config.get("input")
    output_sys = config.get("output")
    value = config.get("value")

    if TypeMatch(input_sys, value) is not True:
        sys.exit("Error: Your given 'value' (" + str(value) + ") does not match your given 'input' (" + str(input_sys) + ") type!")

    #Input control
    

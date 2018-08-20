import sys


class ReverseStringCsv:
    def __init__(self, file_path, separator, verbose=False):
        self.separator = separator
        self.file_name = file_path
        self.verbose = verbose

        file_ending = file_path.split(".")[1]
        file_name = file_path.split(".")[0]
        self.dest_file = file_name + "_reversed." + file_ending
        with open(self.dest_file, "w"):
            pass

    def main(self):
        with open(self.file_name, "r") as f:
            for line in f:
                vals = line.split(self.separator)
                if len(vals) == 2:
                    if vals[1][-1] == "\n":
                        vals[1] = vals[1][:-1]
                if self.verbose: print("Original: " + line)
                # vedno treba sam tadruzga reversat
                string = list(vals[1])
                for i in range(0,len(vals[1]),2):
                    string[i], string[i+1] = string[i+1], string[i]

                vals[1] = ''.join(string)
                ret_line = self.separator.join(vals)
                if len(vals) == 2:
                    ret_line+="\n"
                if self.verbose: print("Obrnjen: " + ret_line)
                if self.verbose: print("")
                with open(self.dest_file, "a") as dst:
                    dst.write(ret_line)


if __name__ == "__main__":
    if len(sys.argv) == 3 or len(sys.argv) == 4:
        if len(sys.argv) == 4:
            if sys.argv[3] == "-v":
                rsc = ReverseStringCsv(sys.argv[1], sys.argv[2], True)
            else:
                print("Obrne 2gi podatek v vrstici in ga shrani v file v isto mapo z istim imenom razen na koncu je _reversed")
                print("Uporaba: python " + sys.argv[0] + " [pot_do_dokumenta] [\"separator\"] [optional: -v]")


        else:
            rsc = ReverseStringCsv(sys.argv[1], sys.argv[2])
        rsc.main()
        print("Obrnjeni podatki so v: " + rsc.dest_file)
    else:
        print("Obrne 2gi podatek v vrstici in ga shrani v file v isto mapo z istim imenom razen na koncu je _reversed")

        print("Uporaba: python " + sys.argv[0] + " [pot_do_dokumenta] [\"separator\"] [optional: -v]")

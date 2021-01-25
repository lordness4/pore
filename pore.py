import os
import argparse




################################################################################ WORKS
# config
config_file = "config.txt"

with open(config_file, "r") as f:
    data = f.read()

f.close()
config = json.loads(data)


################################################################################ WORKS
# handle arguments
parser = argparse.ArgumentParser()

parser.add_argument("--reads1", "-r1",
                    help="<filename> file with forward paired-end reads", required=True)

parser.add_argument("--reads2", "-r2",
                    help="<filename> file with reverse paired-end reads", required=True)

parser.add_argument("--output_dir", "-o",
                    help="<output_dir> directory to store all the resulting files", required=True)

parser.add_argument("--contigs_file", "-c",
                    help="optional <filename> multifasta file containing all contigs assembled form r1 and r2 (skips assembly)")

parser.add_argument("--cleanup",
                    help="optional <TRUE/FALSE> flag. Default=FALSE. If TRUE, all intermediate files will be deleted, in order to save space.")

args = parser.parse_args()

# print help if not enough arguments
if len(sys.argv)<7:
    parser.print_help(sys.stderr)
    exit()


################################################################################
# check arguments given
reads1 = args.reads1
reads2 = args.reads2

if not (os.path.exists(reads1) or os.path.exists(reads2)):
    print("cannot find reads file: ")
    print("either {} or {} not found. ".format(reads1, reads2))
    print("exiting...")
    exit()

output_dir = args.output_dir
output_dir = os.path.abspath(output_dir)

if os.path.exists(output_dir):
    print("output directory already exists: ")
    print("{}".format(output_dir))
    print("exiting...")
    exit()

# contig file given by the user
contig_file = args.contigs_file
# should we clean up afterwards?
cleanup = args.cleanup


################################################################################
# construct the snakemake command



################################################################################
# handle cleanup flag

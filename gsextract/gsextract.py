import click
import gsextract.gse_parser as gse_parser

@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.argument('output_file', type=click.Path())
@click.option('--stream/--no-stream', default=False, help='Stream continuously from the file. Use the --stream flag to dump to a pcap from a real time GSE recording.')
def gsextract(input_file, output_file, stream):
    gse_parser.gse_parse(file=input_file, outfile=output_file, stream=stream)

def cli_runner():
    gsextract()
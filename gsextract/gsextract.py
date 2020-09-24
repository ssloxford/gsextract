import click
import gsextract.gse_parser as gse_parser

@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.argument('output_file', type=click.Path())
@click.option('--stream/--no-stream', default=False, help='Stream continuously from the file. Use the --stream flag to dump to a pcap from a real time GSE recording.')
@click.option('--reliable/--no-reliable', default=True, help='Add the --no-reliable flag to attempt to brute force IP headers in certain situations. Increases recovery but also can result in fake packets.')
def gsextract(input_file, output_file, stream, reliable):
    gse_parser.gse_parse(file=input_file, outfile=output_file, stream=stream, reliable=reliable)

def cli_runner():
    gsextract()
import argparse
import logging
import multiprocessing
import os
import sys

import gentle


def on_progress(p):
    for k,v in p.items():
        logging.debug("%s: %s" % (k, v))


def align(output, audiofile, txtfile, nthreads=4, conservative=False, disfluency=False):

    disfluencies = set(['uh', 'um'])
            
    with open(txtfile, encoding="utf-8") as fh:
        transcript = fh.read()

    resources = gentle.Resources()
    logging.info("converting audio to 8K sampled wav")

    with gentle.resampled(audiofile) as wavfile:
        logging.info("starting alignment")
        aligner = gentle.ForcedAligner(resources, transcript, nthreads=nthreads, disfluency=disfluency, conservative=conservative, disfluencies=disfluencies)
        result = aligner.transcribe(wavfile, progress_cb=on_progress, logging=logging)

    fh = open(output, 'w', encoding="utf-8") if output else sys.stdout
    fh.write(result.to_json(indent=2))
    if output:
        logging.info("output written to %s" % (output))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                                     description='Align a transcript to audio by generating a new language model.  Outputs JSON')
    parser.add_argument(
                        '--nthreads', default=multiprocessing.cpu_count(), type=int,
                        help='number of alignment threads')
    parser.add_argument(
                        '-o', '--output', metavar='output', type=str,
                        help='output filename')
    parser.add_argument(
                        '--conservative', dest='conservative', action='store_true',
                        help='conservative alignment')
    parser.set_defaults(conservative=False)
    parser.add_argument(
                        '--disfluency', dest='disfluency', action='store_true',
                        help='include disfluencies (uh, um) in alignment')
    parser.set_defaults(disfluency=False)
    parser.add_argument(
                        '--log', default="INFO",
                        help='the log level (DEBUG, INFO, WARNING, ERROR, or CRITICAL)')
    parser.add_argument(
                        'audiofile', type=str,
                        help='audio file')
    parser.add_argument(
                        'txtfile', type=str,
                        help='transcript text file')
    args = parser.parse_args()

    log_level = args.log.upper()
    logging.getLogger().setLevel(log_level)
    

    align(nthreads=args.nthreads, output=args.output, conservative=args.conservative, disfluency=args.disfluency, audiofile=args.audiofile, txtfile=args.txtfile)

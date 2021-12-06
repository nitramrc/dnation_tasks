import os
import click
import logging

from src.logger import setup_root_log
from src.matrix import create_matrix
from src.matrix import min_sum


@click.command()
@click.option('-file', '--filepath', default='data/matrix.txt', help='text matrix file path')
def main(**kwargs):
    setup_root_log('matrix_min_sum')
    logger = logging.getLogger('root')

    matrix = create_matrix(kwargs['filepath'])
    logger.info("Min sum of elements for defined direction(right and down) through matrix is {}".
                format(min_sum(matrix)))


if __name__ == "__main__":
    abspath = os.path.abspath(__file__)
    dir_name = os.path.dirname(abspath)
    os.chdir(dir_name)

    main()

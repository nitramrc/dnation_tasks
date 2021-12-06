import csv
import sys
import logging

logger = logging.getLogger('root')


def debug_matrix(matrix):
    logger.debug('----------------------')
    for m in matrix:
        logger.debug(m)
    logger.debug('----------------------')


def create_matrix(file):
    with open(file, "r") as f:
        csv_reader = csv.reader(f, delimiter=',')
        lists_matrix_file = []
        for row in csv_reader:
            for i in range(0, len(row)):
                row[i] = int(row[i])
            lists_matrix_file.append(row)
        matrix = lists_matrix_file
    return matrix


def min_sum(matrix):
    size = len(matrix)
    distance = [[0 for _ in range(size)] for _ in range(size)]
    distance[0][0] = matrix[0][0]

    for i in range(1, size * 2 - 1, 1):
        y = min(i, size - 1)
        x = i - y
        logger.debug("for i:{} x:{} y:{}".format(i, x, y))
        debug_matrix(matrix)
        debug_matrix(distance)
        while x < size and y >= 0:
            logger.debug("while i:{} x:{} y:{}".format(i, x, y))
            debug_matrix(matrix)
            debug_matrix(distance)
            if x > 0:
                move_x = distance[y][x - 1] + matrix[y][x]
                logger.debug("move_x:{}".format(move_x))
            else:
                move_x = sys.maxsize
            if y > 0:
                move_y = distance[y - 1][x] + matrix[y][x]
                logger.debug("move_y:{}".format(move_y))
            else:
                move_y = sys.maxsize
            logger.debug("move_x:{}, move_y:{}".format(move_x, move_y))
            distance[y][x] = min(move_x, move_y)
            x += 1
            y -= 1

    return distance[size - 1][size - 1]

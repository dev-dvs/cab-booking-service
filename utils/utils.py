def compute_distance(source_coordinates: tuple[float, float], destination_coordinates: tuple[float, float]) -> float:
    """
    Compute the Euclidean distance between two points in a 2D space.

    :param source_coordinates: A tuple representing the (latitude, longitude) of the source point.
    :param destination_coordinates: A tuple representing the (latitude, longitude) of the destination point.
    :return: The Euclidean distance between the two points.
    """
    x1, y1 = source_coordinates
    x2, y2 = destination_coordinates
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
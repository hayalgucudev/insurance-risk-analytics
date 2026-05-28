def split_by_category(df, column, group_a, group_b):
    """
    Clean binary segmentation helper
    """
    return (
        df[df[column] == group_a],
        df[df[column] == group_b]
    )
class InsertionError(Exception):
    """Raised when inserting already exisiting city"""
    pass

class DeletionError(Exception):
    """Raised when deleting non-existent city"""
    pass

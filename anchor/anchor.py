"""
Complete set of anchored migration operations
"""

import sys
from django.db import migrations

operation_classes = [
    'AddField', 'AlterField', 'RemoveField', 'RenameField', 'AddIndex', 'AlterIndexTogether',
    'AlterModelManagers', 'AlterModelOptions', 'AlterModelTable', 'AlterOrderWithRespectTo',
    'AlterUniqueTogether', 'CreateModel', 'DeleteModel', 'RemoveIndex', 'RenameModel',
]

anchored_module = sys.modules[__name__]


def factory(base):
    class cls(AnchoredOperation, base):
        pass

    cls.__name__ = '{}'.format(base.__name__)
    cls.__doc__ = '(Anchored) {}'.format(base.__doc__)

    return cls


class AnchoredMigration(migrations.Migration):

    def apply(self, project_state, schema_editor, collect_sql=False):
        return super().apply(project_state, schema_editor, collect_sql)


class AnchoredOperation(object):
    """
    Migrations operation that does not modify the database

    """
    def database_forwards(self, app_label, schema_editor, from_state, to_state):
        """Make no forwards changes of state in the database"""

    def database_backwards(self, app_label, schema_editor, from_state, to_state):
        """Make no backwards changes of state in the database"""


for class_name in operation_classes:
    anchored_operation = factory(getattr(migrations, class_name))
    setattr(anchored_module, anchored_operation.__name__, anchored_operation)

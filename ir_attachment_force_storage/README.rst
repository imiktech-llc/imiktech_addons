Force move attachments to DB storage
====================================

This module is fork <https://github.com/yelizariev/addons-yelizariev/tree/9.0/ir_attachment_force_storage> for odoo 10 support.

In odoo the type of storage is taken from parameter
**ir_attachment.location**. This module move all attachments to a new
storage type (**db** or **file**) everytime you edit or create the parameter via Settings\\Parameters\\System Parameters menu.

Right after installing **ir_attachment.location** is set to **db**.

To rollback everything, before uninstalling the module set  **ir_attachment.location** to **file**.

Technical implementation
------------------------

We use fixed built-in force_storage function to update location for existing attachments.


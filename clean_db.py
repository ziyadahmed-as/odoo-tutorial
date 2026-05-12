import psycopg2

try:
    conn = psycopg2.connect("dbname='odoomanage' user='odoo' password='odoo' host='127.0.0.1' port='5432'")
    cur = conn.cursor()
    # Delete ir_model_data references for ir.ui.view related to beltech.project
    cur.execute("DELETE FROM ir_model_data WHERE model='ir.ui.view' AND res_id IN (SELECT id FROM ir_ui_view WHERE model='beltech.project')")
    # Delete the views themselves
    cur.execute("DELETE FROM ir_ui_view WHERE model='beltech.project'")
    # Also delete the old actions just in case
    cur.execute("DELETE FROM ir_model_data WHERE model='ir.actions.act_window' AND res_id IN (SELECT id FROM ir_act_window WHERE res_model='beltech.project')")
    cur.execute("DELETE FROM ir_act_window WHERE res_model='beltech.project'")
    conn.commit()
    cur.close()
    conn.close()
    print("Successfully deleted old views and actions.")
except Exception as e:
    print(f"Error: {e}")

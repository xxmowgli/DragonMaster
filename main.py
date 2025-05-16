import json
import os
import tkinter as tk
import secrets
from tkinter import filedialog, messagebox
from tkinter import ttk

item_name_map = {
    "2rxJ495rm0GDn4h5OWKiyQ": "Ash Logs",
    "CxUwQN-Me0qnNfyc207f0g": "Blisterwood",
    "zm9DtUc8ieNZpWe7ioL_KA": "Goblin Pack",
    "gunABauXjk6khTFVIKifoA": "Silver Bar",
    "Y2Y48OMHukKIilN4srd7cA": "Bronze Bar",
    "52QCB0uSNJD0UoC21lRJvA": "Vault Core",
    "T8l7pktHUJoUuxi9mkrT7g": "Vault Shard",
    "SNCcLEdRbF7GAwSkvob6NQ": "Hearty Stew",
    "hKYyX0vQ_pgLRAi2ugGK3w": "Clean Water",
    "uYBo5UuEdMMdOyicMA9ikQ": "Meat Stew2",
    "Ng6eFNNuiU-VdxSoZtI6kA": "Iron Bar",
    "GHBDsEGyH5DJpTqa7xIC1w": "Abyssal Spine",
    "ISwwk0SMdhURciK1Sr3i6Q": "Coarse Animal Hide",
    "Gv_wHkJnBgiXOfq0cCvggg": "Ash Plank",
    "guCjkksBOmEcLFut-VH-qg": "Stone Gravel",
    "FcnXn0Sq3OS7tJKuCRAc1A": "Other Gravel",
    "TsGMyBWLNEWhBdNu21CwCA": "Oak Log",
    "qOY004ZJaEaR8DmcDqB2KA": "Rune Essence",
    "ukjoSEXQTWbO6zSJvP5Z4Q": "AntiPoison Pot",
    "GC6S207zgsmHryqJEdEQaQ": "RuneArmourthing",
    "Dns4MEGuhT5fcRWocI5o9Q": "Thread",
    "DJIQWUsnDB7Umey0E2dFgA": "Swamp Tar",
    "vgsjm0jT19zFn1uH9N2Rbg": "Wool Thread",
    "qRA1TEfZJkMoanWXc_l-Sg": "weak Health Pot",
    "2vSF4Se4MkWaZG0pHYcb8g": "Fang Arrow",
    "D-BzgHFSHkyc53teVzmBNA": "Gold Ore",
    "9jFU2lh9l0qPbNTspGCBFA": "Gold Bar",
    "GQcT3TAgK0ulDFXjsp-k1A": "cloth1",
    "6kYeY05XaTnhySas_bXdnw": "cloth2",
    "Jf2AM4PfnUqwTuW0cPXheA": "wool cloth",
    "-jEah0znNr-2UVmbHK-Hqg": "DwellBerry infusion",
    "1-eS15sb9UW_8kRzIMyV6g": "iron arrow",
    "igveHUWYg2AeXe69EwW1PA": "Ferocious Infusion",
    "cZ6va0BSo6_5Dg2Pi23lUQ": "Evasive Infusion",
    "PZdR5E2sYqyUe-2JgBsCfA": "fleet-flooted infusion",
    "u9KamEevDhDoqA-Ypsobrw": "Attack Pot",
    "-9Zin0B1C7GQgVKwKSR0hQ": "Health Pot",
    "ab53An3iPkyjTqnHyme-0A": "Animal Hide Scrap",
    "3wV1xUv5zBDHRiaAk2qv7w": "Whetstone",
    "mZWtu9Ir9ECtl0a7cV7uJw": "Fleece",
    "QpxVI0bu8fcLkpuM7HrEaw": "dried dwellberries",
    "HwM2_HvXZUyt8FmT4F2iYQ": "potato",
    "1k8-cj3JqEGeRgu1P7PK2g": "raw rat meat",
    "GHxAwJ8gNkSe3vxloWof2A": "redberries",
    "QfPOk0c4rF6PIUqOxt0ytg": "meat pizza",
    "FPYmOkCqcOpLYpaP1DKYjA": "peach",
    "yEEiukHPM7htB4WeWEXeWg": "fried onions",
    "0aufkk55nHU1TlSAXZ0o3g": "rat roast",
    "xawyKY4sAkmNcNuINCw3ww": "silver ore",
    "LURhZ0Q6FaLGzh-siBuT7g": "wild anima",
    "XII5rkqVhw9I3sWWZNKteA": "garou pack",
    "NeMd5ktRmFW1ZWqnCwsxKA": "flank steak",
    "EHN6Hs9NFkur7chZVfchJg": "cabbaged",
    "sGZHV0IIuJLCDIyGNNBMbA": "dried redberries",
    "Ua7XqsiwjUio_H540eRegw": "raw game meat",
    "O9t9Kknjb4lXvNKsNl7Vrg": "fortifying soup",
    "tosPpUxp9FZgwdGvvXrcjw": "raw bestial meat",
    "DQdI2EZLlP0EJB2C6_R28w": "fried cabbage",
    "CPT7I01jfIBmhyCQLJH31A": "weak focused artisan",
    "_a30PUP3vGbK6omuRTvw2Q": "soft animal fur",
    "xAyLrEN_5B3KGXOjhpGzrg": "small wardstone",
    "rTRm3cGOmUm1h1BMEYzTwA": "iron ore",
    "gC-ZukCFUhIWbCyJIkj3LQ": "steak",
    "A8Lx3sZhHEeG4GXsl4ZLZw": "copper ore",
    "u-HYwkRw-MdC8hSQnS84Vw": "medium wardstone",
    "h1AqBkRETk-Fu_65W6BjVw": "tin ore",
    "wgV3TEOkcYod4tGRdutHqg": "baked potato",
    "8gh6wkTHrHGgAMSeSMHNTw": "weak focused mining pot",
    "U3WBak2LNdsGzrajcaLGpw": "weak focused wookdcutting pot",
    "K7le0EXS_TjIx-Wb9d9PZg": "weak focused cooking pot",
    "0PXPSUTx8SdrxW6J26Ljfw": "weak focused runecrafting pot",
    "AEnD3ErsJVZ3V7WT1YdPQQ": "antlers",
    "6lzGokw1exVCJAmMfnUnkg": "shocking plant bulb",
    "vxn3aEpxraaQXJi9Btd7Cw": "poison plant blub",
    "OQisqk4_V81aRxSm8IjMMg": "clay slab",
    "JsMp30dRbfOXIPuy-4NmFA": "onion",
    "6VtTq32kQkyOk-E3Ly05-A": "raw bird meat",
    "EWuEEEhBQ59daI2TL5y9YQ": "small animal fang",
    "xhvDCkkTzJPbihGOZo3Hvw": "clay vessel unfired",
    "1k8-cj3JqEGeRgu1P7PK2g": "raw rat meat",
    "Ttc6u0zyAi-JMaOjrxwtNQ": "raw farm meat",
    "Br8lTU45wX65kDigZkkgAg": "fuel briquette",
    "z-xbJy9IS0iWNNx9WciARQ": "vine root",
    "zEg0M0VWEp6-wLOhkvYJ8A": "clay mould",
    "tKokB0xYm6tJNHiWwmG2SQ": "anima infued bark",
    "v5MSO2Wz4ke5xOGvKC5GlQ": "feathers",
    "uTmDj0pXttZKU7qob4UvNw": "clay vessel",
    "RdhNn0ebpZZIPQqMviMjNg": "sandstone",
    "qelCL0cKP9oFmYaJkKg6wA": "dragon tooth",
    "FXYVR0dXwrzmeo-goNwTHA": "clay mould unfired",
    "E5lUJEc3VidsqDGPkYhl4A": "ram horn",
    "qwgPgkOGqffCUdG9M7YR2Q": "molten glass",
    "EK3fckHjkrHbATuNLd9Jhg": "clay slab unfired",
    "C-Blv0bNk7v6BOWLA8Cw-g": "clay dec",
    "sycphkkEs4cXKKC721kS2w": "clay dec unfired",
    "7MA-NkEejSNBooCvO4XI9w": "monstrous fang"
    
}

gear_name_map = {
    "P3_Aq0nAXu5dlFuBNGgyaw": "Abyssal Whip",
    "RyuOEkWEWdGcvQqo2dPOgA": "Antidragon Shield",
    "_oShik-jE3kWgsG82AEuNQ": "blightwood shortBow",
    "Hcq0C0UjvN3n8q-X2uqa7w": "staff Of Light",
    "YvBVZjzx_UKN9z1wIPzlrA": "Iron Axe",
    "VfaynRGcAkammV5YUusfbA": "Iron Pickaxe",
    "lWGe1hSwiECAS9xhsMzJfg": "Torch",
    "gIoZIUIT52OUDkGFuzSBlw": "Wild Archer Cowel",
    "fr5LJkUvJRZ-DbqVbKaB4w": "Wild Archer Body",
    "l6qWl0-xTPdrhweMah3eTg": "Wild Archer Chaps",
    "71LhGUmAvrlALY6KcS8W3Q": "Fractured Cape",
    "3LufGUl5SzS2zV2Vj7QCPg": "T4 Poison Dagger",
    "FK7SwEPmPfVFztSXScvKQA": "Crystal Bow",
    "s7HI6EmvRXRq7T69epFpxg": "Hunters Stagbow",
    "hThLR2Lk6kODfRRmAs4YBQ": "Iron Mace",
    "o9zzhev_YEulDWv5D8vI3A": "Iron Warhammer",
    "h0jHf-hTx0KeGyukdCnN4Q": "Wizard hat",
    "2-okKxsy7k-FRgP-vgQEQA": "wizard robe",
    "FlnNkilo_EyfB0gbqf32AQ": "wizard robe legs",
    "h3G7NqBW-0i6TrNRlBD6Sg": "apprentice hat",
    "g9vfX7KsMkurrMZa7z1aPg": "apprentice robe",
    "AIZLP8mwfEij7hwWUOr-aQ": "apprentice leggings",
    "lhrErX7MF0q9XlhdPdhCrA": "bronze helmet",
    "N2kAI3uQgki-eP0rIoHYhQ": "bronze platebody",
    "wQPcKK1XV0iF1_CADXUwEw": "bronze platelegs",
    "PxHJuE6PgUKY-zugyUXSUQ": "iron helmet",
    "CAtRgsni70SltXq4uzs6Yg": "iron platebody",
    "lWABtugu90SEqpE70Gf8ew": "iron platelegs",
    "GutTdkwskIsX75i6-CilJA": "dragonkin mage hood",
    "rXtN2EZOq9NpnL-WyVpF8Q": "dragonkid mage robe",
    "uDBybUNuv5UipiSXb8BG-A": "dragonkin mage robe legs",
    "5PEcXkJHZY9PDqKb9Skqww": "paladin's helm",
    "0LL6JE9-pi2e3VSDOwqqYw": "paladin's platebody",
    "mkSObERGptKuVly00uIfTQ": "paladin's platelegs",
    "YvIen0_ZFiR1Kn-5ucQrDA": "reinforced helmet",
    "mkaB7UQN1fBbSkGNVTVRZw": "reinforced body",
    "GZuI4kHd7c-hpqWq5Nbdpw": "reinforced platelegs",
    "wLzThnOQEUaw90mBnn8QTw": "hard leather cowl",
    "h7tqvcgrDk2iGdD7TYwiSA": "hard leather body",
    "7Ajx5nOVUUW6l8nU2YiLOA": "hard leather chaps",
    "YVvQRk9Uv1a4PceWi3985w": "studded leather cowl",
    "eAqy2E05wXWCK4O5s2Dnwg": "studded leather body",
    "bZAEoUISHmuQXu6HlIFIyQ": "studded leather chaps",
    "-mOez0ZysUa2kkuZQY4s0w": "leather cowl",
    "Q6DUGmTWNkG5S1Ki_5Nz1w": "leather chaps",
    "XT0Zft6J30iLvjVNxnzw6Q": "leather body",
    "FK7SwEPmPfVFztSXScvKQA": "crystal bow",
    "ARf7DUYPa_AlyLOOsnTIYw": "thane's authority",
    "9QZ0eUU7xVxKhq-_nMoCcQ": "dark mage robes",
    "hWGilEcAZgtX2JWejH4ncA": "dark mage robe legs",
    "M3Y6KEIGYrsnS8-j5ewQxw": "dark mage hood",
    "3LufGUl5SzS2zV2Vj7QCPg": "T4 poison dagger",
    "NA76rEFl7Di8f5aFj_L3SA": "T3 poison Dagger",
    "924KFU8kvGNESi-zN0doDw": "ash battlestaff",
    "s7HI6EmvRXRq7T69epFpxg": "hunter's stagbow",
    "ALn1jUyxkFwgIHmHAGkoxg": "draconic staff",
    "hS_GuEyi70Xf932m1rq7PA": "gireving moon staff",
    "GO-fJEIf4N7Y0EeG5D0YSw": "t2 burning dagger",
    "CN1GVEgi8t_uRs-yFmH_FQ": "t4 burning dagger",
    "g7aQPfflM0q63qyJZyWI8w": "oak shortbow",
    "NqTlRkd7Zw4BE9GM_mDbtw": "wild scout's shortbow",
    "IJILMByu-kCq_0feZkzKBw": "stone club",
    "o9zzhev_YEulDWv5D8vI3A": "iron warhammer",
    "yvkI8EKmmaD8zT-a7IVqOA": "blightwood battlestaff",
    "8ivfA0axvgaP1smick68pw": "oak battlestaff",
    "lJqTrE_r-nkdhwyoPhfsAA": "bronze mace",
    "OJSTGEEY6uNu4beRiM4Qvw": "goblin swingslash",
    "djtTEkaTg3ARdre_xsNXCg": "bone club",
    "VVq58NyN8EKOk3WUg2130Q": "adventerurs longbow",
    "eqrPvUI8qhvjnbGRoIxNug": "bronze sword",
    "lHKVrkMlSsZx5lKVZRH63Q": "chieftains blade",
    "gFA3V8-Y5UGLPAtJKYNnTw": "iron sword",
    "UW6yfU2tUde27I2aZB9JHA": "t2 poison dagger",
    "-ahw20RwuJqFDsKcOrryNQ": "t4 bleeding dagger",
    "P4DqJ03JPXW9Uf-z9vf9cA": "t1 burning dagger",
    "f5pdM9IkUU2dZp0okjecuA": "stone dagger",
    "AQ-JQEAJEyOWJKuGTq7KCQ": "t2 bleeding dagger",
    "yte2PUYaqeYZH02J_aviEg": "granite maul",
    "jWfoPkWonpdDzBWYUQ1qPg": "t3 bleeding dagger",
    "UBB8W0_AMoWP5yKf7M9KRw": "oak longbow",
    "4bMdm0gvxNqxKSaQjGtFmQ": "dragonbane dagger",
    "pmx4j0E3SP9r4gmY38QrYA": "t1 shock dagger",
    "PPvgBkmqKmyUwki-TAtqig": "t3 shock dagger",
    "d-s3s5ciWkSi_Q4p-XaMoA": "iron greataxe",
    "PSWEV0JzVwxsalWCFqPbOw": "bronze greatsword",
    "XWOefkcc3bliVpWrsPMokg": "skullsplitter"
}

# Add rune name mapping
rune_name_map = {
    "Dvo6TE2d7YNnoni8XbKYzw": "Air Rune",
    "bbLdJRhwPEWt1ScENYRUCg": "Water Rune",
    "lCE7i3iXGUuHv7FphIOcXg": "Earth Rune",
    "_QMgbMYhjU-9jAD_euFbyQ": "Fire Rune",
    "iKbF7k2XvufGqqyg5rK-vQ": "Nature Rune",  # Add placeholder ID
    "_c9JTkwKy8s88GWv586hbQ": "Law Rune",        # Add placeholder ID
    "4wdYZE-FFMhS9Iia0ftWDg": "Astral Rune"   # Add placeholder ID
}

json_files = []
current_inventory_data = {}
current_file_path = None

# Create separate lists for items and gear
regular_items = ["Empty"] + sorted(list(item_name_map.values()))
gear_items = ["Empty"] + sorted(list(gear_name_map.values()))

# Initialize the slot entries list
slot_entries = []

# Initialize the rune entries list
rune_entries = []

# Initialize the skill labels list
skill_labels = []

# Initialize the slot checkboxes list
slot_checkboxes = []

# Create a list of rune names for the dropdown
rune_items = ["Empty"] + sorted(list(rune_name_map.values()))

# Add this near the top with other color definitions
RS_SELECTED_BORDER = '#FFD700'  # Gold color for selected slots

def update_slot_border(slot_frame, regular_var, gear_var):
    # Get the current item (gear takes precedence)
    current_item = gear_var.get() if gear_var.get() != "Empty" else regular_var.get()
    
    # Update border color based on whether slot has an item
    if current_item != "Empty":
        slot_frame.configure(bg=RS_FILLED_BORDER)
    else:
        slot_frame.configure(bg=RS_EMPTY_BORDER)

def update_current_item_label(label, regular_var, gear_var):
    # Get the current item (gear takes precedence)
    current_item = gear_var.get() if gear_var.get() != "Empty" else regular_var.get()
    label.configure(text=current_item)

def on_item_select(event, regular_var, gear_var, slot_frame, is_regular=True):
    # Clear the other dropdown when one is selected
    if is_regular:
        if regular_var.get() != "Empty":
            gear_var.set("Empty")
    else:
        if gear_var.get() != "Empty":
            regular_var.set("Empty")
    
    # Update the slot border
    update_slot_border(slot_frame, regular_var, gear_var)

def update_rune_slot_border(slot_frame, rune_var):
    # Update border color based on whether slot has a rune
    if rune_var.get() != "Empty":
        slot_frame.configure(bg=RS_FILLED_BORDER)
    else:
        slot_frame.configure(bg=RS_EMPTY_BORDER)

def update_current_rune_label(label, rune_var):
    label.configure(text=rune_var.get())

def on_rune_select(event, rune_var, slot_frame, current_rune_label):
    # Update the current rune label
    update_current_rune_label(current_rune_label, rune_var)
    # Update the slot border
    update_rune_slot_border(slot_frame, rune_var)

def load_json():
    global current_inventory_data, current_file_path
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if not file_path:
        return

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load JSON file: {e}")
        return

    current_inventory_data = data
    current_file_path = file_path
    file_name = os.path.basename(file_path)

    if file_name not in json_files:
        json_files.append(file_name)

    # Clear all checkboxes first
    for checkbox_var in slot_checkboxes:
        checkbox_var.set(False)

    refresh_display()

def set_all_slots():
    editor = tk.Toplevel(root)
    editor.title("Set All Slots")
    editor.geometry("300x250")
    style_editor_window(editor)

    combined_map = {**item_name_map, **gear_name_map}

    tk.Label(editor, text="Set All Slots", font=("Arial", 12, "bold")).pack(pady=5)

    tk.Label(editor, text="Item:").pack()
    item_var = tk.StringVar()
    item_choices = list(combined_map.values())
    item_dropdown = tk.OptionMenu(editor, item_var, *item_choices)
    item_dropdown.pack()

    tk.Label(editor, text="Count/Durability:").pack()
    count_entry = tk.Entry(editor)
    count_entry.pack()

    # Set default values
    item_var.set(item_choices[0])
    count_entry.insert(0, "1")

    def apply_all():
        item_name = item_var.get()
        count = count_entry.get()
        try:
            count = int(count)
        except:
            messagebox.showerror("Error", "Count must be a number.")
            return

        item_id = next((k for k, v in combined_map.items() if v == item_name), None)
        if not item_id:
            messagebox.showerror("Error", "Item not found.")
            return

        for i in range(32):
            guid = secrets.token_urlsafe(16)
            slot_key = str(i)
            if item_id in gear_name_map:
                current_inventory_data.setdefault("Inventory", {})[slot_key] = {
                    "GUID": guid,
                    "ItemData": item_id,
                    "Durability": count,
                    "VitalShield": 0
                }
            else:
                current_inventory_data.setdefault("Inventory", {})[slot_key] = {
                    "GUID": guid,
                    "ItemData": item_id,
                    "Count": count
                }

        editor.destroy()
        refresh_display()

    tk.Button(editor, text="✅ Apply to All Slots", command=apply_all).pack(pady=10)

def save_inventory_to_file():
    if not current_file_path or not current_inventory_data:
        messagebox.showwarning("No file", "No JSON file loaded.")
        return

    # Clear existing inventory data
    current_inventory_data["Inventory"] = {}
    
    # Save inventory entries (slots 0-31)
    for i, (regular_var, gear_var, count_entry, current_item_label) in enumerate(slot_entries):
        regular_item = regular_var.get()
        gear_item = gear_var.get()
        count_text = count_entry.get()
        
        # Determine which item to use (gear takes precedence if both are set)
        item_name = gear_item if gear_item != "Empty" else regular_item
        
        if item_name and item_name != "Empty":
            try:
                # Convert count to integer and ensure it's at least 1
                count = max(1, int(count_text))
                
                # Find the item ID from the name
                item_id = None
                if item_name in gear_name_map.values():
                    item_id = next((k for k, v in gear_name_map.items() if v.lower() == item_name.lower()), None)
                else:
                    item_id = next((k for k, v in item_name_map.items() if v.lower() == item_name.lower()), None)
                
                if item_id:
                    guid = secrets.token_urlsafe(16)
                    if item_id in gear_name_map:
                        current_inventory_data["Inventory"][str(i)] = {
                            "GUID": guid,
                            "ItemData": item_id,
                            "Durability": count,
                            "VitalShield": 0
                        }
                    else:
                        current_inventory_data["Inventory"][str(i)] = {
                            "GUID": guid,
                            "ItemData": item_id,
                            "Count": count
                        }
            except ValueError:
                continue

    # Save rune entries (slots 33-64)
    for i, (rune_var, count_entry, current_rune_label) in enumerate(rune_entries):
        rune_name = rune_var.get()
        count_text = count_entry.get()
        
        if rune_name and rune_name != "Empty":
            try:
                # Convert count to integer and ensure it's at least 1
                count = max(1, int(count_text))
                
                # Find the rune ID from the name
                rune_id = next((k for k, v in rune_name_map.items() if v.lower() == rune_name.lower()), None)
                
                if rune_id:
                    guid = secrets.token_urlsafe(16)
                    # Add VitalShield for Fire and Air runes
                    if rune_name in ["Fire Rune", "Air Rune"]:
                        current_inventory_data["Inventory"][str(i + 33)] = {
                            "GUID": guid,
                            "ItemData": rune_id,
                            "Count": count,
                            "VitalShield": 0
                        }
                    else:
                        current_inventory_data["Inventory"][str(i + 33)] = {
                            "GUID": guid,
                            "ItemData": rune_id,
                            "Count": count
                        }
            except ValueError:
                continue

    # Initialize Loadout if it doesn't exist
    if "Loadout" not in current_inventory_data:
        current_inventory_data["Loadout"] = {}
    
    print("\nSaving loadout items:")  # Debug print
    # Save loadout entries (slots 0-4)
    for i, (item_var, count_entry, current_item_label) in enumerate(loadout_entries):
        item_name = item_var.get()
        count_text = count_entry.get()
        
        print(f"Processing loadout slot {i}: {item_name}")  # Debug print
        
        if item_name and item_name != "Empty":
            try:
                # Convert count to integer and ensure it's at least 1
                count = max(1, int(count_text))
                
                # Find the item ID from the name (case-insensitive)
                item_id = next((k for k, v in gear_name_map.items() if v.lower() == item_name.lower()), None)
                
                if item_id:
                    guid = secrets.token_urlsafe(16)
                    current_inventory_data["Loadout"][str(i)] = {
                        "GUID": guid,
                        "ItemData": item_id,
                        "Durability": count,
                        "VitalShield": 0
                    }
                    print(f"Saved loadout slot {i} with item {item_name} (ID: {item_id})")  # Debug print
                else:
                    print(f"Could not find item ID for {item_name}")  # Debug print
            except ValueError as e:
                print(f"Error saving loadout slot {i}: {e}")  # Debug print
                continue
        else:
            # If slot is empty, remove it from the loadout data
            if str(i) in current_inventory_data["Loadout"]:
                del current_inventory_data["Loadout"][str(i)]
            print(f"Loadout slot {i} is empty")  # Debug print
    
    # Set MaxSlotIndex for loadout
    current_inventory_data["Loadout"]["MaxSlotIndex"] = 4

    # Find max slot index by checking all inventory slots
    max_slot_index = -1
    for slot_key in current_inventory_data["Inventory"].keys():
        try:
            slot_index = int(slot_key)
            if slot_index > max_slot_index:
                max_slot_index = slot_index
        except ValueError:
            continue

    print(f"Max slot index found: {max_slot_index}")  # Debug print

    # Set the MaxSlotIndex inside the Inventory object
    current_inventory_data["Inventory"]["MaxSlotIndex"] = max_slot_index

    # Save skills data
    if "Skills" not in current_inventory_data:
        current_inventory_data["Skills"] = {"Skills": []}
    else:
        current_inventory_data["Skills"]["Skills"] = []

    # ID to Name mapping for skills
    skill_names = {
        "Wf3i7Ha-B06DH719j1vtBw": "Artisan",
        "4pefO9k1lUqfA6mvHNi1SA": "Attack",
        "waK-8EyQFQ2xEjCGYmuTRQ": "Construction",
        "Tn7t6DQyX0-Q0cM5K7B90A": "Cooking",
        "0hreSMRVXUihq9qjDO2CFA": "Magic/Ranged",
        "jqX0Gh6QI0GFFPCDFK_CJQ": "Mining",
        "heq7u88Q2UuLXFqLGTVwQw": "Magic/Ranged",
        "NOqC-z-2ckqi0El22qMFlw": "Runecrafting",
        "4zYUGF5u_0KbMLkWJmmBbQ": "Woodcutting"
    }

    # Save current skills state from UI
    for row_frame in skill_labels:
        name_label = row_frame.winfo_children()[0]
        xp_entry = row_frame.winfo_children()[1]
        
        skill_name = name_label.cget("text").rstrip(":")
        xp_text = xp_entry.get()
        
        try:
            xp = int(xp_text)
            # For Magic/Ranged, save both IDs
            if skill_name == "Magic/Ranged":
                current_inventory_data["Skills"]["Skills"].extend([
                    {"Id": "0hreSMRVXUihq9qjDO2CFA", "Xp": xp},
                    {"Id": "heq7u88Q2UuLXFqLGTVwQw", "Xp": xp}
                ])
            else:
                # Find the skill ID from the name for other skills
                skill_id = next((k for k, v in skill_names.items() if v == skill_name), None)
                if skill_id:
                    current_inventory_data["Skills"]["Skills"].append({
                        "Id": skill_id,
                        "Xp": xp
                    })
        except ValueError:
            continue

    print("\nFinal loadout data:")  # Debug print
    print(json.dumps(current_inventory_data["Loadout"], indent=2))  # Debug print

    try:
        with open(current_file_path, 'w') as f:
            json.dump(current_inventory_data, f, indent=4)
        messagebox.showinfo("Success", "Inventory, runes, and skills updated and saved.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save file: {e}")

def save_preset():
    # Create a new data structure from current UI state
    preset_data = {
        "Inventory": {},
        "Loadout": {},
        "Skills": {"Skills": []}
    }
    
    # ID to Name mapping for skills
    skill_names = {
        "Wf3i7Ha-B06DH719j1vtBw": "Artisan",
        "4pefO9k1lUqfA6mvHNi1SA": "Attack",
        "waK-8EyQFQ2xEjCGYmuTRQ": "Construction",
        "Tn7t6DQyX0-Q0cM5K7B90A": "Cooking",
        "0hreSMRVXUihq9qjDO2CFA": "Magic/Ranged",
        "jqX0Gh6QI0GFFPCDFK_CJQ": "Mining",
        "heq7u88Q2UuLXFqLGTVwQw": "Magic/Ranged",
        "NOqC-z-2ckqi0El22qMFlw": "Runecrafting",
        "4zYUGF5u_0KbMLkWJmmBbQ": "Woodcutting"
    }
    
    # Save current inventory state from UI
    for i, (regular_var, gear_var, count_entry, current_item_label) in enumerate(slot_entries):
        regular_item = regular_var.get()
        gear_item = gear_var.get()
        count_text = count_entry.get()
        
        # Determine which item to use (gear takes precedence if both are set)
        item_name = gear_item if gear_item != "Empty" else regular_item
        
        if item_name and item_name != "Empty":
            try:
                count = int(count_text)
                # Find the item ID from the name
                item_id = None
                if item_name in gear_name_map.values():
                    item_id = next((k for k, v in gear_name_map.items() if v.lower() == item_name.lower()), None)
                else:
                    item_id = next((k for k, v in item_name_map.items() if v.lower() == item_name.lower()), None)
                
                if item_id:
                    guid = secrets.token_urlsafe(16)
                    if item_id in gear_name_map:
                        preset_data["Inventory"][str(i)] = {
                            "GUID": guid,
                            "ItemData": item_id,
                            "Durability": count,
                            "VitalShield": 0
                        }
                    else:
                        preset_data["Inventory"][str(i)] = {
                            "GUID": guid,
                            "ItemData": item_id,
                            "Count": count
                        }
            except ValueError:
                continue

    # Save current loadout state from UI
    for i, (item_var, count_entry, current_item_label) in enumerate(loadout_entries):
        item_name = item_var.get()
        count_text = count_entry.get()
        
        if item_name and item_name != "Empty":
            try:
                count = int(count_text)
                # Find the item ID from the name (case-insensitive)
                item_id = next((k for k, v in gear_name_map.items() if v.lower() == item_name.lower()), None)
                
                if item_id:
                    guid = secrets.token_urlsafe(16)
                    preset_data["Loadout"][str(i)] = {
                        "GUID": guid,
                        "ItemData": item_id,
                        "Durability": count,
                        "VitalShield": 0
                    }
            except ValueError:
                continue
    
    # Set MaxSlotIndex for loadout
    preset_data["Loadout"]["MaxSlotIndex"] = 4

    # Save current skills state from UI
    for row_frame in skill_labels:
        name_label = row_frame.winfo_children()[0]
        xp_entry = row_frame.winfo_children()[1]
        
        skill_name = name_label.cget("text").rstrip(":")
        xp_text = xp_entry.get()
        
        try:
            xp = int(xp_text)
            # For Magic/Ranged, save both IDs
            if skill_name == "Magic/Ranged":
                preset_data["Skills"]["Skills"].extend([
                    {"Id": "0hreSMRVXUihq9qjDO2CFA", "Xp": xp},
                    {"Id": "heq7u88Q2UuLXFqLGTVwQw", "Xp": xp}
                ])
            else:
                # Find the skill ID from the name for other skills
                skill_id = next((k for k, v in skill_names.items() if v == skill_name), None)
                if skill_id:
                    preset_data["Skills"]["Skills"].append({
                        "Id": skill_id,
                        "Xp": xp
                    })
        except ValueError:
            continue

    # Ask user where to save the preset
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
        title="Save Preset"
    )
    
    if not file_path:
        return

    try:
        with open(file_path, 'w') as f:
            json.dump(preset_data, f, indent=4)
        messagebox.showinfo("Success", "Preset saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save preset: {e}")

def load_preset():
    # Ask user to select a preset file
    file_path = filedialog.askopenfilename(
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
        title="Load Preset"
    )
    
    if not file_path:
        return

    try:
        # Load the preset data
        with open(file_path, 'r') as f:
            preset_data = json.load(f)
        
        # ID to Name mapping for skills
        skill_names = {
            "Wf3i7Ha-B06DH719j1vtBw": "Artisan",
            "4pefO9k1lUqfA6mvHNi1SA": "Attack",
            "waK-8EyQFQ2xEjCGYmuTRQ": "Construction",
            "Tn7t6DQyX0-Q0cM5K7B90A": "Cooking",
            "0hreSMRVXUihq9qjDO2CFA": "Magic/Ranged",
            "jqX0Gh6QI0GFFPCDFK_CJQ": "Mining",
            "heq7u88Q2UuLXFqLGTVwQw": "Magic/Ranged",
            "NOqC-z-2ckqi0El22qMFlw": "Runecrafting",
            "4zYUGF5u_0KbMLkWJmmBbQ": "Woodcutting"
        }
        
        # Clear current UI state and set all borders to red
        for i, (regular_var, gear_var, count_entry, current_item_label) in enumerate(slot_entries):
            regular_var.set("Empty")
            gear_var.set("Empty")
            count_entry.delete(0, tk.END)
            count_entry.insert(0, "0")
            current_item_label.configure(text="Empty")
            
            # Set all slot borders to red initially
            slot_frame = inventory_frame.grid_slaves(row=i // 8, column=i % 8)[0]
            slot_frame.configure(bg=RS_EMPTY_BORDER)
        
        # Clear loadout entries
        for item_var, count_entry, current_item_label in loadout_entries:
            item_var.set("Empty")
            count_entry.delete(0, tk.END)
            count_entry.insert(0, "0")
            current_item_label.configure(text="Empty")
            
            # Set all loadout slot borders to red initially
            slot_frame = loadout_frame.grid_slaves(row=loadout_entries.index((item_var, count_entry, current_item_label)) // 3, 
                                                 column=loadout_entries.index((item_var, count_entry, current_item_label)) % 3)[0]
            slot_frame.configure(bg=RS_EMPTY_BORDER)
        
        # Load inventory data to UI
        for slot_str, item in preset_data.get("Inventory", {}).items():
            try:
                slot_index = int(slot_str)
                if 0 <= slot_index < 32:
                    item_id = item.get("ItemData", "Unknown ID")
                    item_name = None
                    
                    # Find item name from ID
                    if item_id in gear_name_map:
                        item_name = gear_name_map[item_id]
                    elif item_id in item_name_map:
                        item_name = item_name_map[item_id]
                    
                    if item_name:
                        regular_var, gear_var, count_entry, current_item_label = slot_entries[slot_index]
                        
                        # Set the appropriate dropdown based on item type
                        if item_id in gear_name_map:
                            gear_var.set(item_name)
                            regular_var.set("Empty")
                            count_entry.delete(0, tk.END)
                            count_entry.insert(0, str(item.get("Durability", 0)))
                        else:
                            regular_var.set(item_name)
                            gear_var.set("Empty")
                            count_entry.delete(0, tk.END)
                            count_entry.insert(0, str(item.get("Count", 0)))
                        
                        # Update the current item label
                        current_item_label.configure(text=item_name)
                        
                        # Update the slot border to green for filled slots
                        slot_frame = inventory_frame.grid_slaves(row=slot_index // 8, column=slot_index % 8)[0]
                        slot_frame.configure(bg=RS_FILLED_BORDER)
            except Exception as e:
                print(f"Error loading slot {slot_str}: {e}")
                continue
        
        # Load loadout data to UI
        for slot_str, item in preset_data.get("Loadout", {}).items():
            try:
                slot_index = int(slot_str)
                if 0 <= slot_index < 5:  # Loadout slots 0-4
                    item_id = item.get("ItemData", "Unknown ID")
                    item_name = gear_name_map.get(item_id, f"Unknown Item ({item_id})")
                    
                    item_var, count_entry, current_item_label = loadout_entries[slot_index]
                    item_var.set(item_name)
                    
                    durability = item.get("Durability", "???")
                    count_entry.delete(0, tk.END)
                    count_entry.insert(0, str(durability))
                    
                    current_item_label.configure(text=item_name)
                    
                    # Update the slot border
                    slot_frame = loadout_frame.grid_slaves(row=slot_index // 3, column=slot_index % 3)[0]
                    slot_frame.configure(bg=RS_FILLED_BORDER)
            except ValueError as e:
                if slot_str != "MaxSlotIndex":  # Skip MaxSlotIndex as it's not a slot
                    print(f"Error loading loadout slot {slot_str}: {e}")
                continue
        
        # Load skills data to UI
        for skill in preset_data.get("Skills", {}).get("Skills", []):
            skill_id = skill.get("Id")
            xp = skill.get("Xp", 0)
            
            # Find the skill row with matching ID
            for row_frame in skill_labels:
                name_label = row_frame.winfo_children()[0]
                xp_entry = row_frame.winfo_children()[1]
                
                # Check both Magic/Ranged IDs
                if (skill_names.get(skill_id) == name_label.cget("text").rstrip(":") or
                    (skill_id in ["0hreSMRVXUihq9qjDO2CFA", "heq7u88Q2UuLXFqLGTVwQw"] and 
                     name_label.cget("text").rstrip(":") == "Magic/Ranged")):
                    xp_entry.delete(0, tk.END)
                    xp_entry.insert(0, str(xp))
                    break
        
        messagebox.showinfo("Success", "Preset loaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load preset: {e}")

def refresh_display():
    combined_map = {**item_name_map, **gear_name_map}
    
    # Clear all entries and update borders
    for i, (regular_var, gear_var, count_entry, current_item_label) in enumerate(slot_entries):
        regular_var.set("Empty")
        gear_var.set("Empty")
        count_entry.delete(0, tk.END)
        count_entry.insert(0, "0")
        current_item_label.configure(text="Empty")
        
        # Update the slot border to red for empty slots
        slot_frame = inventory_frame.grid_slaves(row=i // 8, column=i % 8)[0]
        slot_frame.configure(bg=RS_EMPTY_BORDER)
    
    # Clear rune entries
    for rune_var, count_entry, current_rune_label in rune_entries:
        rune_var.set("Empty")
        count_entry.delete(0, tk.END)
        count_entry.insert(0, "0")
        current_rune_label.configure(text="Empty")
        
        # Update the slot border to red for empty slots
        slot_frame = rune_frame.grid_slaves(row=rune_entries.index((rune_var, count_entry, current_rune_label)) // 8, 
                                          column=rune_entries.index((rune_var, count_entry, current_rune_label)) % 8)[0]
        slot_frame.configure(bg=RS_EMPTY_BORDER)

    # Clear loadout entries
    for item_var, count_entry, current_item_label in loadout_entries:
        item_var.set("Empty")
        count_entry.delete(0, tk.END)
        count_entry.insert(0, "0")
        current_item_label.configure(text="Empty")
        
        # Update the slot border to red for empty slots
        slot_frame = loadout_frame.grid_slaves(row=loadout_entries.index((item_var, count_entry, current_item_label)) // 3, 
                                             column=loadout_entries.index((item_var, count_entry, current_item_label)) % 3)[0]
        slot_frame.configure(bg=RS_EMPTY_BORDER)

    # Update inventory entries
    for slot_str, item in current_inventory_data.get("Inventory", {}).items():
        try:
            slot_index = int(slot_str)
            if 0 <= slot_index < 32:  # Regular inventory slots
                item_id = item.get("ItemData", "Unknown ID")
                item_name = combined_map.get(item_id, f"Unknown Item ({item_id})")
                
                regular_var, gear_var, count_entry, current_item_label = slot_entries[slot_index]
                
                # Set the appropriate dropdown based on item type
                if item_id in gear_name_map:
                    gear_var.set(item_name)
                    regular_var.set("Empty")
                else:
                    regular_var.set(item_name)
                    gear_var.set("Empty")
                
                # Update the current item label
                current_item_label.configure(text=item_name)
                
                # Update the slot border to green for filled slots
                slot_frame = inventory_frame.grid_slaves(row=slot_index // 8, column=slot_index % 8)[0]
                slot_frame.configure(bg=RS_FILLED_BORDER)

                if item_id in gear_name_map:
                    durability = item.get("Durability", "???")
                    count_entry.delete(0, tk.END)
                    count_entry.insert(0, str(durability))
                else:
                    count = item.get("Count", 0)
                    count_entry.delete(0, tk.END)
                    count_entry.insert(0, str(count))
            elif 33 <= slot_index < 65:  # Rune slots
                item_id = item.get("ItemData", "Unknown ID")
                rune_name = rune_name_map.get(item_id, f"Unknown Rune ({item_id})")
                count = item.get("Count", 0)
                
                rune_index = slot_index - 33
                if 0 <= rune_index < len(rune_entries):
                    rune_var, count_entry, current_rune_label = rune_entries[rune_index]
                    rune_var.set(rune_name)
                    count_entry.delete(0, tk.END)
                    count_entry.insert(0, str(count))
                    current_rune_label.configure(text=rune_name)
                    
                    # Update the slot border
                    slot_frame = rune_frame.grid_slaves(row=rune_index // 8, column=rune_index % 8)[0]
                    slot_frame.configure(bg=RS_FILLED_BORDER)
        except Exception as e:
            print(f"Error updating slot {slot_str}: {e}")
            continue

    # Update loadout entries
    for slot_str, item in current_inventory_data.get("Loadout", {}).items():
        try:
            slot_index = int(slot_str)
            if 0 <= slot_index < 5:  # Loadout slots 0-4
                item_id = item.get("ItemData", "Unknown ID")
                item_name = gear_name_map.get(item_id, f"Unknown Item ({item_id})")
                
                item_var, count_entry, current_item_label = loadout_entries[slot_index]
                item_var.set(item_name)
                
                durability = item.get("Durability", "???")
                count_entry.delete(0, tk.END)
                count_entry.insert(0, str(durability))
                
                current_item_label.configure(text=item_name)
                
                # Update the slot border
                slot_frame = loadout_frame.grid_slaves(row=slot_index // 3, column=slot_index % 3)[0]
                slot_frame.configure(bg=RS_FILLED_BORDER)
                
                print(f"Updated loadout slot {slot_index} with {item_name}")  # Debug print
        except ValueError as e:
            if slot_str != "MaxSlotIndex":  # Skip MaxSlotIndex as it's not a slot
                print(f"Error updating loadout slot {slot_str}: {e}")
            continue
    
    # Refresh skills display
    refresh_skills_display()

def refresh_skills_display():
    for label in skill_labels:
        label.destroy()
    skill_labels.clear()

    for widget in skills_display_frame.winfo_children():
        widget.destroy()

    # Get skills data from current_inventory_data
    skills_data = current_inventory_data.get("Skills", {}).get("Skills", [])

    # ID to Name mapping
    skill_names = {
        "Wf3i7Ha-B06DH719j1vtBw": "Artisan",
        "4pefO9k1lUqfA6mvHNi1SA": "Attack",
        "waK-8EyQFQ2xEjCGYmuTRQ": "Construction",
        "Tn7t6DQyX0-Q0cM5K7B90A": "Cooking",
        "0hreSMRVXUihq9qjDO2CFA": "Magic/Ranged",
        "jqX0Gh6QI0GFFPCDFK_CJQ": "Mining",
        "heq7u88Q2UuLXFqLGTVwQw": "Magic/Ranged",
        "NOqC-z-2ckqi0El22qMFlw": "Runecrafting",
        "4zYUGF5u_0KbMLkWJmmBbQ": "Woodcutting"
    }

    # Track which skills we've displayed
    displayed_skills = set()

    # Display all skills
    for skill in skills_data:
        skill_id = skill.get("Id", "Unknown")
        xp = skill.get("Xp", 0)
        skill_name = skill_names.get(skill_id, "Unknown")

        # Skip if we've already displayed this skill (except for Magic/Ranged)
        if skill_name in displayed_skills and skill_id not in ["0hreSMRVXUihq9qjDO2CFA", "heq7u88Q2UuLXFqLGTVwQw"]:
            continue

        # For Magic/Ranged, only skip if we've already displayed both IDs
        if skill_id in ["0hreSMRVXUihq9qjDO2CFA", "heq7u88Q2UuLXFqLGTVwQw"]:
            if "0hreSMRVXUihq9qjDO2CFA" in displayed_skills and "heq7u88Q2UuLXFqLGTVwQw" in displayed_skills:
                continue

        displayed_skills.add(skill_id)

        row_frame = tk.Frame(skills_display_frame, bg=RS_LIGHT_TAN)
        row_frame.pack(fill="x", pady=2)

        # Skill name label
        name_label = tk.Label(row_frame, text=f"{skill_name}:", 
                            width=15, anchor="w",
                            bg=RS_LIGHT_TAN, fg='black',
                            font=('RuneScape UF', 9))
        name_label.pack(side="left")

        # XP entry
        xp_entry = tk.Entry(row_frame, width=10,
                          bg=RS_LIGHT_TAN, fg='black',
                          font=('RuneScape UF', 9))
        xp_entry.insert(0, str(xp))
        xp_entry.pack(side="left", padx=5)

        # MAX button
        def set_max_xp(entry=xp_entry):
            entry.delete(0, tk.END)
            entry.insert(0, "55000")

        max_button = tk.Button(row_frame, text="MAX",
                             command=lambda e=xp_entry: set_max_xp(e),
                             bg=RS_DARK_TAN, fg=RS_GOLD,
                             font=('RuneScape UF', 8, 'bold'),
                             width=4)
        max_button.pack(side="left", padx=2)

        skill_labels.append(row_frame)

def style_editor_window(window):
    window.configure(bg=RS_BROWN)
    for widget in window.winfo_children():
        if isinstance(widget, tk.Label):
            widget.configure(bg=RS_BROWN, fg=RS_GOLD, font=('RuneScape UF', 10))
        elif isinstance(widget, tk.Button):
            widget.configure(bg=RS_DARK_TAN, fg=RS_GOLD, font=('RuneScape UF', 10, 'bold'))
        elif isinstance(widget, tk.Entry):
            widget.configure(bg=RS_LIGHT_TAN, fg='black', font=('RuneScape UF', 10))
        elif isinstance(widget, tk.OptionMenu):
            widget.configure(bg=RS_DARK_TAN, fg=RS_GOLD, font=('RuneScape UF', 10))

def insert_to_checked_slots():
    # Get the selected item and count from the combobox
    item_name = item_dropdown.get()  # Changed from item_var.get() to item_dropdown.get()
    count_text = count_var.get()
    
    print(f"\nSelected item: '{item_name}'")  # Debug print with quotes to see spaces
    print(f"Selected count: {count_text}")  # Debug print
    
    if item_name == "Empty":
        messagebox.showerror("Error", "Please select an item from the dropdown.")
        return
    
    try:
        count = int(count_text)
    except ValueError:
        messagebox.showerror("Error", "Count must be a number.")
        return
    
    # Find the item ID from the name (case-insensitive)
    item_id = None
    
    # Debug prints for item lookup
    print("\nChecking gear_name_map:")
    print("Available gear items:")
    for k, v in gear_name_map.items():
        print(f"  '{v}'")
        if v.lower() == item_name.lower():
            print(f"Found match: '{v}' -> {k}")
            item_id = k
            break
    
    if not item_id:
        print("\nChecking item_name_map:")
        print("Available regular items:")
        for k, v in item_name_map.items():
            print(f"  '{v}'")
            if v.lower() == item_name.lower():
                print(f"Found match: '{v}' -> {k}")
                item_id = k
                break
    
    if not item_id:
        print(f"\nNo match found for '{item_name}'")
        messagebox.showerror("Error", f"Item not found: '{item_name}'")
        return
    
    print(f"\nFound item_id: {item_id}")
    
    # Update all checked slots
    checked_count = 0
    for i, (checkbox, slot_frame) in enumerate(zip(slot_checkboxes, inventory_frame.grid_slaves())):
        if checkbox.get():
            checked_count += 1
            print(f"Updating checked slot {i}")
            regular_var, gear_var, count_entry, current_item_label = slot_entries[i]
            
            # Get the exact name from the map to ensure case matches
            exact_name = gear_name_map.get(item_id) if item_id in gear_name_map else item_name_map.get(item_id)
            if not exact_name:
                print(f"Warning: Could not find exact name for item_id {item_id}")
                exact_name = item_name
            
            if item_id in gear_name_map:
                gear_var.set(exact_name)
                regular_var.set("Empty")
                print(f"Set as gear item: '{exact_name}'")
            else:
                regular_var.set(exact_name)
                gear_var.set("Empty")
                print(f"Set as regular item: '{exact_name}'")
            
            count_entry.delete(0, tk.END)
            count_entry.insert(0, str(count))
            current_item_label.configure(text=exact_name)
            
            # Update the slot border
            slot_frame.configure(bg=RS_FILLED_BORDER)
    
    print(f"Updated {checked_count} slots")

def toggle_checkbox(slot_frame, checkbox_var):
    # Toggle the checkbox state
    checkbox_var.set(not checkbox_var.get())
    
    # Get the slot index from the frame's grid info
    grid_info = slot_frame.grid_info()
    slot_index = grid_info['row'] * 8 + grid_info['column']
    
    # Get the current item state from slot_entries
    regular_var, gear_var, _, _ = slot_entries[slot_index]
    regular_item = regular_var.get()
    gear_item = gear_var.get()
    current_item = gear_item if gear_item != "Empty" else regular_item
    
    # Debug print
    print(f"Toggle Slot {slot_index}: Regular={regular_item}, Gear={gear_item}, Current={current_item}")
    
    # Update the border color based on selection and item state
    if checkbox_var.get():
        slot_frame.configure(bg=RS_SELECTED_BORDER)
        print(f"Setting slot {slot_index} to gold (selected)")
    else:
        # Set border color based on whether slot is empty
        if current_item != "Empty":
            slot_frame.configure(bg=RS_FILLED_BORDER)
            print(f"Setting slot {slot_index} to green (filled)")
        else:
            slot_frame.configure(bg=RS_EMPTY_BORDER)
            print(f"Setting slot {slot_index} to red (empty)")

def clear_all_selections():
    # Clear all checkboxes and reset borders
    for i in range(32):  # We know we have 32 slots
        checkbox_var = slot_checkboxes[i]
        checkbox_var.set(False)
        
        # Get the slot frame directly using grid coordinates
        slot_frame = inventory_frame.grid_slaves(row=i // 8, column=i % 8)[0]
        
        # Get the current item state
        regular_var, gear_var, _, _ = slot_entries[i]
        regular_item = regular_var.get()
        gear_item = gear_var.get()
        current_item = gear_item if gear_item != "Empty" else regular_item
        
        # Debug print
        print(f"Slot {i}: Regular={regular_item}, Gear={gear_item}, Current={current_item}")
        
        # Set border color based on whether slot is empty
        if current_item != "Empty":
            slot_frame.configure(bg=RS_FILLED_BORDER)
            print(f"Setting slot {i} to green (filled)")
        else:
            slot_frame.configure(bg=RS_EMPTY_BORDER)
            print(f"Setting slot {i} to red (empty)")

def load_rune_pack():
    # Define rune slots in order (only the ones we want to load)
    rune_order = [
        "Air Rune",
        "Water Rune",
        "Earth Rune",
        "Fire Rune",
        "Nature Rune",
        "Law Rune",
        "Astral Rune"
    ]
    
    # Clear existing runes first
    for rune_var, count_entry, _ in rune_entries:
        rune_var.set("Empty")
        count_entry.delete(0, tk.END)
        count_entry.insert(0, "0")
    
    # Set each rune slot
    for i, rune_name in enumerate(rune_order):
        if i < len(rune_entries):
            rune_var, count_entry, current_rune_label = rune_entries[i]
            rune_var.set(rune_name)
            count_entry.delete(0, tk.END)
            count_entry.insert(0, "9999")
            current_rune_label.configure(text=rune_name)
            
            # Update the slot border
            slot_frame = rune_frame.grid_slaves(row=i // 8, column=i % 8)[0]
            slot_frame.configure(bg=RS_FILLED_BORDER)

def clear_all_runes():
    for i, (rune_var, count_entry, current_rune_label) in enumerate(rune_entries):
        rune_var.set("Empty")
        count_entry.delete(0, tk.END)
        count_entry.insert(0, "0")
        current_rune_label.configure(text="Empty")
        
        # Update the slot border
        slot_frame = rune_frame.grid_slaves(row=i // 8, column=i % 8)[0]
        slot_frame.configure(bg=RS_EMPTY_BORDER)

def clear_all_backpack_slots():
    for i, (regular_var, gear_var, count_entry, current_item_label) in enumerate(slot_entries):
        regular_var.set("Empty")
        gear_var.set("Empty")
        count_entry.delete(0, tk.END)
        count_entry.insert(0, "0")
        current_item_label.configure(text="Empty")
        
        # Update the slot border
        slot_frame = inventory_frame.grid_slaves(row=i // 8, column=i % 8)[0]
        slot_frame.configure(bg=RS_EMPTY_BORDER)

# Create the main window and set up the UI
root = tk.Tk()
root.title("DragonMaster v0.1 May 2025")
root.geometry("1500x900")
root.configure(bg='#2B1810')  # Dark brown background like RuneScape

# Define RuneScape-style colors
RS_BROWN = '#2B1810'  # Dark brown background
RS_GOLD = '#FFD700'   # Gold for important text
RS_TAN = '#D2B48C'    # Tan for backgrounds
RS_DARK_TAN = '#8B4513'  # Dark tan for buttons
RS_LIGHT_TAN = '#F5DEB3'  # Light tan for text backgrounds
RS_RED = '#8B0000'    # Dark red for danger/warning
RS_GREEN = '#006400'  # Dark green for success
RS_EMPTY_BORDER = '#8B0000'  # Reddish brown for empty slots
RS_FILLED_BORDER = '#556B2F'  # Greenish brown for filled slots

# Configure default styles
style = ttk.Style()
style.configure('RS.TButton', 
    background=RS_DARK_TAN,
    foreground=RS_GOLD,
    font=('RuneScape UF', 10, 'bold'),
    padding=5
)

# Top Control Panel
control_frame = tk.Frame(root, bg=RS_BROWN)
control_frame.pack(fill=tk.X, pady=5)

# Style the buttons
load_btn = tk.Button(control_frame, text="📂 Load JSON File", command=load_json,
                    bg=RS_DARK_TAN, fg=RS_GOLD, font=('RuneScape UF', 10, 'bold'),
                    relief='raised', borderwidth=2)
load_btn.pack(side=tk.LEFT, padx=5)

save_btn = tk.Button(control_frame, text="💾 Update Inventory File", command=save_inventory_to_file,
                    bg=RS_DARK_TAN, fg=RS_GOLD, font=('RuneScape UF', 10, 'bold'),
                    relief='raised', borderwidth=2)
save_btn.pack(side=tk.LEFT, padx=5)

save_preset_btn = tk.Button(control_frame, text="💾 Save Preset", command=save_preset,
                    bg=RS_DARK_TAN, fg=RS_GOLD, font=('RuneScape UF', 10, 'bold'),
                    relief='raised', borderwidth=2)
save_preset_btn.pack(side=tk.LEFT, padx=5)

load_preset_btn = tk.Button(control_frame, text="💾 Load Preset", command=load_preset,
                    bg=RS_DARK_TAN, fg=RS_GOLD, font=('RuneScape UF', 10, 'bold'),
                    relief='raised', borderwidth=2)
load_preset_btn.pack(side=tk.LEFT, padx=5)

# Main Top Frame for two boxes
top_frame = tk.Frame(root, bg=RS_BROWN)
top_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

# Left Box (Equipment)
box1 = tk.Frame(top_frame, bg=RS_TAN, bd=2, relief='ridge')
box1.pack(side="left", expand=False, fill="both", padx=5)

# Right Box (Skills Pane)
skills_pane = tk.Frame(top_frame, bg=RS_TAN, bd=2, relief='ridge')
skills_pane.pack(side="left", expand=True, fill="both", padx=5)

# Skills Display Inside Skills Pane
skills_display_frame = tk.Frame(skills_pane, bg=RS_LIGHT_TAN, bd=2, relief='groove')
skills_display_frame.pack(padx=10, pady=10, fill="both", expand=True)

# Inventory Bar
inventory_container = tk.Frame(root, bg=RS_BROWN)
inventory_container.pack(side="bottom", fill="x", padx=10, pady=10)

# Style the notebook
style = ttk.Style()
style.theme_use('default')  # Reset to default theme first
style.configure('TNotebook', background=RS_BROWN)
style.configure('TNotebook.Tab', 
    background=RS_BROWN,
    foreground=RS_GOLD,
    padding=[10, 2],
    font=('RuneScape UF', 10, 'bold'))
style.map('TNotebook.Tab',
    background=[('selected', RS_RED), ('!selected', RS_BROWN)],
    foreground=[('selected', RS_GOLD), ('!selected', RS_GOLD)],
    lightcolor=[('selected', RS_RED), ('!selected', RS_BROWN)],
    darkcolor=[('selected', RS_RED), ('!selected', RS_BROWN)],
    bordercolor=[('selected', RS_RED), ('!selected', RS_BROWN)])

# Create the notebook (tabbed interface) for inventory
notebook = ttk.Notebook(inventory_container)
notebook.pack(fill=tk.BOTH, expand=True)

# Create three frames for the inventory tabs
inventory_tab = tk.Frame(notebook, bg=RS_BROWN)
tab2 = tk.Frame(notebook, bg=RS_BROWN)
tab3 = tk.Frame(notebook, bg=RS_BROWN)

# Add the tabs to the notebook
notebook.add(inventory_tab, text='📦 Backpack')
notebook.add(tab2, text='📦 Runes')
notebook.add(tab3, text='📦 Loadout')

# Create bulk insert control panel for inventory
bulk_insert_frame = tk.Frame(inventory_tab, bg=RS_BROWN)
bulk_insert_frame.pack(fill=tk.X, pady=5)

# Create variables for bulk insert
item_var = tk.StringVar(value="Empty")
count_var = tk.StringVar(value="1")

# Create dropdown and entry for bulk insert
item_label = tk.Label(bulk_insert_frame, text="Item:", bg=RS_BROWN, fg=RS_GOLD, font=('RuneScape UF', 10))
item_label.pack(side=tk.LEFT, padx=5)

item_dropdown = ttk.Combobox(bulk_insert_frame, textvariable=item_var, values=regular_items + gear_items, width=20, state='readonly')
item_dropdown.pack(side=tk.LEFT, padx=5)

count_label = tk.Label(bulk_insert_frame, text="Count:", bg=RS_BROWN, fg=RS_GOLD, font=('RuneScape UF', 10))
count_label.pack(side=tk.LEFT, padx=5)

count_entry = tk.Entry(bulk_insert_frame, textvariable=count_var, width=6, bg=RS_LIGHT_TAN, fg='black', font=('RuneScape UF', 10))
count_entry.pack(side=tk.LEFT, padx=5)

insert_btn = tk.Button(bulk_insert_frame, text="Insert to Checked Slots", command=insert_to_checked_slots,
                      bg=RS_DARK_TAN, fg=RS_GOLD, font=('RuneScape UF', 10, 'bold'),
                      relief='raised', borderwidth=2)
insert_btn.pack(side=tk.LEFT, padx=5)

clear_selections_btn = tk.Button(bulk_insert_frame, text="Clear Selections", command=clear_all_selections,
                               bg=RS_DARK_TAN, fg=RS_GOLD, font=('RuneScape UF', 10, 'bold'),
                               relief='raised', borderwidth=2)
clear_selections_btn.pack(side=tk.LEFT, padx=5)

# Add clear slots button to the bulk insert frame
clear_slots_btn = tk.Button(bulk_insert_frame, text="Clear Slots", command=clear_all_backpack_slots,
                           bg=RS_DARK_TAN, fg=RS_GOLD, font=('RuneScape UF', 10, 'bold'),
                           relief='raised', borderwidth=2)
clear_slots_btn.pack(side=tk.LEFT, padx=5)

# Inventory Grid for first tab
inventory_frame = tk.Frame(inventory_tab, bg=RS_BROWN)
inventory_frame.pack()

# Create a frame for the inventory grid title
inventory_title_frame = tk.Frame(inventory_tab, bg=RS_BROWN)
inventory_title_frame.pack()
inventory_label = tk.Label(inventory_title_frame, text="Backpack", 
                         bg=RS_BROWN, fg=RS_GOLD, 
                         font=('RuneScape UF', 12, 'bold'))
inventory_label.pack()

# Create rune grid for second tab
rune_frame = tk.Frame(tab2, bg=RS_BROWN)
rune_frame.pack()

# Create a frame for the rune grid title
rune_title_frame = tk.Frame(tab2, bg=RS_BROWN)
rune_title_frame.pack()
rune_label = tk.Label(rune_title_frame, text="Runes", 
                     bg=RS_BROWN, fg=RS_GOLD, 
                     font=('RuneScape UF', 12, 'bold'))
rune_label.pack()

# Create rune slots (from slot 33 onwards)
for i in range(33, 65):  # Create slots 33-64
    # Create a frame for each rune slot
    slot_frame = tk.Frame(rune_frame, bg=RS_EMPTY_BORDER, relief='ridge', bd=2)
    slot_frame.grid(row=(i-33) // 8, column=(i-33) % 8, padx=1, pady=1)
    
    # Inner frame for content
    inner_frame = tk.Frame(slot_frame, bg=RS_TAN)
    inner_frame.pack(fill='both', expand=True, padx=1, pady=1)
    
    # Slot number label
    slot_label = tk.Label(inner_frame, 
                         text=f"Slot {i}",
                         bg=RS_TAN,
                         fg='black',
                         font=('RuneScape UF', 8))
    slot_label.pack(anchor='nw')
    
    # Create variables for the rune slot
    rune_var = tk.StringVar(value="Empty")
    
    # Rune combobox
    rune_combo = ttk.Combobox(inner_frame, 
                             textvariable=rune_var,
                             values=rune_items,
                             width=10,
                             state='readonly')
    rune_combo.pack(fill='x', padx=1)
    
    # Current rune label
    current_rune_label = tk.Label(inner_frame,
                                 text="Empty",
                                 bg=RS_TAN,
                                 fg='black',
                                 font=('RuneScape UF', 8),
                                 wraplength=90)
    current_rune_label.pack(fill='x', padx=1)
    
    # Count entry
    count_entry = tk.Entry(inner_frame,
                          width=6,
                          bg=RS_LIGHT_TAN,
                          fg='black',
                          font=('RuneScape UF', 8))
    count_entry.pack(fill='x', padx=1)
    
    # Bind events
    rune_combo.bind('<<ComboboxSelected>>', 
                   lambda e, r=rune_var, s=slot_frame, l=current_rune_label: 
                   on_rune_select(e, r, s, l))
    
    # Update current rune label when selection changes
    def update_current_rune(*args):
        update_current_rune_label(current_rune_label, rune_var)
        update_rune_slot_border(slot_frame, rune_var)
    
    rune_var.trace('w', update_current_rune)
    
    # Add to rune entries list
    rune_entries.append((rune_var, count_entry, current_rune_label))

# Now create the slots after all frames are defined
for i in range(32):
    # Create a frame for each slot
    slot_frame = tk.Frame(inventory_frame, bg=RS_EMPTY_BORDER, relief='ridge', bd=2)
    slot_frame.grid(row=i // 8, column=i % 8, padx=1, pady=1)
    
    # Inner frame for content
    inner_frame = tk.Frame(slot_frame, bg=RS_TAN)
    inner_frame.pack(fill='both', expand=True, padx=1, pady=1)
    
    # Create a frame for the checkbox and label
    checkbox_frame = tk.Frame(inner_frame, bg=RS_TAN)
    checkbox_frame.pack(anchor='nw', fill='x')
    
    # Checkbox for bulk operations
    checkbox_var = tk.BooleanVar(value=False)
    checkbox = tk.Checkbutton(checkbox_frame, variable=checkbox_var, bg=RS_TAN)
    checkbox.pack(side='left')
    slot_checkboxes.append(checkbox_var)
    
    # Slot number label
    slot_label = tk.Label(checkbox_frame, 
                         text=f"Slot {i+1}",
                         bg=RS_TAN,
                         fg='black',
                         font=('RuneScape UF', 8))
    slot_label.pack(side='left')
    
    # Make both the checkbox frame and its contents clickable
    def make_clickable(widget, sf=slot_frame, cv=checkbox_var):
        widget.bind('<Button-1>', lambda e, s=sf, c=cv: toggle_checkbox(s, c))
    
    make_clickable(checkbox_frame)
    make_clickable(checkbox)
    make_clickable(slot_label)
    
    # Create a frame for the dropdowns
    dropdown_frame = tk.Frame(inner_frame, bg=RS_TAN)
    dropdown_frame.pack(fill='x', padx=1)
    
    # Create both variables first
    regular_var = tk.StringVar(value="Empty")
    gear_var = tk.StringVar(value="Empty")
    
    # Regular items combobox
    regular_combo = ttk.Combobox(dropdown_frame, 
                                textvariable=regular_var,
                                values=regular_items,
                                width=10,
                                state='readonly')
    regular_combo.pack(side='left', fill='x', expand=True, padx=1)
    
    # Gear items combobox
    gear_combo = ttk.Combobox(dropdown_frame, 
                             textvariable=gear_var,
                             values=gear_items,
                             width=10,
                             state='readonly')
    gear_combo.pack(side='left', fill='x', expand=True, padx=1)
    
    # Current item label
    current_item_label = tk.Label(inner_frame,
                                 text="Empty",
                                 bg=RS_TAN,
                                 fg='black',
                                 font=('RuneScape UF', 8),
                                 wraplength=90)
    current_item_label.pack(fill='x', padx=1)
    
    # Bind events after both comboboxes are created
    regular_combo.bind('<<ComboboxSelected>>', 
                      lambda e, r=regular_var, g=gear_var, s=slot_frame, l=current_item_label: 
                      (on_item_select(e, r, g, s, True), update_current_item_label(l, r, g)))
    gear_combo.bind('<<ComboboxSelected>>', 
                   lambda e, r=regular_var, g=gear_var, s=slot_frame, l=current_item_label: 
                   (on_item_select(e, r, g, s, False), update_current_item_label(l, r, g)))
    
    # Update current item label when selection changes
    def update_current_item(*args):
        update_current_item_label(current_item_label, regular_var, gear_var)
        update_slot_border(slot_frame, regular_var, gear_var)
    
    regular_var.trace('w', update_current_item)
    gear_var.trace('w', update_current_item)
    
    # Count entry
    count_entry = tk.Entry(inner_frame,
                          width=6,
                          bg=RS_LIGHT_TAN,
                          fg='black',
                          font=('RuneScape UF', 8))
    count_entry.pack(fill='x', padx=1)
    
    slot_entries.append((regular_var, gear_var, count_entry, current_item_label))

# Configure ttk style for comboboxes
style = ttk.Style()
style.configure('TCombobox', 
                fieldbackground=RS_LIGHT_TAN,
                background=RS_LIGHT_TAN,
                foreground='black',
                arrowcolor='black',
                selectbackground=RS_DARK_TAN,
                selectforeground=RS_GOLD)

# Modify the rune tab section to add the new buttons
# Find the rune_title_frame section and add after it:
rune_control_frame = tk.Frame(tab2, bg=RS_BROWN)
rune_control_frame.pack(pady=5)

load_rune_pack_btn = tk.Button(rune_control_frame, text="Load Rune Pack", command=load_rune_pack,
                              bg=RS_DARK_TAN, fg=RS_GOLD, font=('RuneScape UF', 10, 'bold'),
                              relief='raised', borderwidth=2)
load_rune_pack_btn.pack(side=tk.LEFT, padx=5)

clear_runes_btn = tk.Button(rune_control_frame, text="Clear Runes", command=clear_all_runes,
                           bg=RS_DARK_TAN, fg=RS_GOLD, font=('RuneScape UF', 10, 'bold'),
                           relief='raised', borderwidth=2)
clear_runes_btn.pack(side=tk.LEFT, padx=5)

# Add contact section at the bottom
contact_frame = tk.Frame(root, bg=RS_BROWN)
contact_frame.pack(side="bottom", fill="x", pady=5)

# Create a frame for the contact info
contact_info_frame = tk.Frame(contact_frame, bg=RS_BROWN)
contact_info_frame.pack(side="right", padx=10)

# Discord link
discord_frame = tk.Frame(contact_info_frame, bg=RS_BROWN)
discord_frame.pack(side="left", padx=5)

discord_icon = tk.Label(discord_frame, text="💬", 
                       bg=RS_BROWN, fg=RS_GOLD,
                       font=('RuneScape UF', 12))
discord_icon.pack(side="left", padx=2)

discord_text = tk.Label(discord_frame, text="Discord",
                       bg=RS_BROWN, fg=RS_GOLD,
                       font=('RuneScape UF', 10))
discord_text.pack(side="left")

# GitHub link
github_frame = tk.Frame(contact_info_frame, bg=RS_BROWN)
github_frame.pack(side="left", padx=5)

github_icon = tk.Label(github_frame, text="📦", 
                      bg=RS_BROWN, fg=RS_GOLD,
                      font=('RuneScape UF', 12))
github_icon.pack(side="left", padx=2)

github_text = tk.Label(github_frame, text="GitHub",
                      bg=RS_BROWN, fg=RS_GOLD,
                      font=('RuneScape UF', 10))
github_text.pack(side="left")

# Donation link
donation_frame = tk.Frame(contact_info_frame, bg=RS_BROWN)
donation_frame.pack(side="left", padx=5)

donation_icon = tk.Label(donation_frame, text="💝", 
                        bg=RS_BROWN, fg=RS_GOLD,
                        font=('RuneScape UF', 12))
donation_icon.pack(side="left", padx=2)

donation_text = tk.Label(donation_frame, text="Donate",
                        bg=RS_BROWN, fg=RS_GOLD,
                        font=('RuneScape UF', 10))
donation_text.pack(side="left")

# Make the contact sections clickable
def open_discord(event):
    import webbrowser
    webbrowser.open("https://discord.gg/TeZvrV8728")

def open_github(event):
    import webbrowser
    webbrowser.open("https://github.com/xxmowgli/DragonMaster")

def open_donation(event):
    import webbrowser
    webbrowser.open("https://www.xxmowgli.co.uk")

# Bind click events
discord_icon.bind('<Button-1>', open_discord)
discord_text.bind('<Button-1>', open_discord)
github_icon.bind('<Button-1>', open_github)
github_text.bind('<Button-1>', open_github)
donation_icon.bind('<Button-1>', open_donation)
donation_text.bind('<Button-1>', open_donation)

# Add these after the existing item maps but before the UI creation

# Loadout slot item lists
loadout_hat_items = [
    "Empty",
    "Paladin's Helm",
    "Reinforced Helmet",
    "Hard Leather Cowl",
    "Studded Leather Cowl",
    "Leather Cowl",
    "Wizard Hat",
    "Apprentice Hat",
    "Dragonkin Mage Hood",
    "Dark Mage Hood"
]

loadout_body_items = [
    "Empty",
    "Paladin's Platebody",
    "Reinforced Body",
    "Hard Leather Body",
    "Studded Leather Body",
    "Leather Body",
    "Wizard Robe",
    "Apprentice Robe",
    "Dragonkin Mage Robe",
    "Dark Mage Robbes"
]

loadout_legs_items = [
    "Empty",
    "Paladin's Platelegs",
    "Reinforced Platelegs",
    "Hard Leather Chaps",
    "Studded Leather Chaps",
    "Leather Chaps",
    "Wizard Robe Legs",
    "Apprentice Leggings",
    "Dragonkin Mage Robe Legs",
    "Dark Mage Robe Legs"
]

loadout_cape_items = [
    "Empty",
    "Fractured Cape"
]

loadout_jewelry_items = [
    "Empty"
]

# Add this function after the existing functions but before the UI creation
def update_loadout_slot_border(slot_frame, item_var):
    if item_var.get() != "Empty":
        slot_frame.configure(bg=RS_FILLED_BORDER)
    else:
        slot_frame.configure(bg=RS_EMPTY_BORDER)

def on_loadout_item_select(event, item_var, slot_frame, current_item_label):
    update_loadout_item_label(current_item_label, item_var)
    update_loadout_slot_border(slot_frame, item_var)

# Add this after creating the notebook tabs but before creating the inventory grid
# Create loadout grid for third tab
loadout_frame = tk.Frame(tab3, bg=RS_BROWN)
loadout_frame.pack()

# Create a frame for the loadout grid title
loadout_title_frame = tk.Frame(tab3, bg=RS_BROWN)
loadout_title_frame.pack()
loadout_label = tk.Label(loadout_title_frame, text="Equipment Loadout", 
                        bg=RS_BROWN, fg=RS_GOLD, 
                        font=('RuneScape UF', 12, 'bold'))
loadout_label.pack()

# Create loadout slots (5 slots)
loadout_entries = []
slot_names = ["Hat", "Body", "Legs", "Cape", "Jewelry"]
slot_items = [loadout_hat_items, loadout_body_items, loadout_legs_items, 
              loadout_cape_items, loadout_jewelry_items]

for i in range(5):
    # Create a frame for each loadout slot
    slot_frame = tk.Frame(loadout_frame, bg=RS_EMPTY_BORDER, relief='ridge', bd=2)
    slot_frame.grid(row=i // 3, column=i % 3, padx=1, pady=1)
    
    # Inner frame for content
    inner_frame = tk.Frame(slot_frame, bg=RS_TAN)
    inner_frame.pack(fill='both', expand=True, padx=1, pady=1)
    
    # Slot name label
    slot_label = tk.Label(inner_frame, 
                         text=f"{slot_names[i]}",
                         bg=RS_TAN,
                         fg='black',
                         font=('RuneScape UF', 8))
    slot_label.pack(anchor='nw')
    
    # Create variables for the loadout slot
    item_var = tk.StringVar(value="Empty")
    
    # Item combobox
    item_combo = ttk.Combobox(inner_frame, 
                             textvariable=item_var,
                             values=slot_items[i],
                             width=15,
                             state='readonly')
    item_combo.pack(fill='x', padx=1)
    
    # Current item label
    current_item_label = tk.Label(inner_frame,
                                 text="Empty",
                                 bg=RS_TAN,
                                 fg='black',
                                 font=('RuneScape UF', 8),
                                 wraplength=90)
    current_item_label.pack(fill='x', padx=1)
    
    # Durability entry
    count_entry = tk.Entry(inner_frame,
                          width=6,
                          bg=RS_LIGHT_TAN,
                          fg='black',
                          font=('RuneScape UF', 8))
    count_entry.pack(fill='x', padx=1)
    
    # Bind events
    item_combo.bind('<<ComboboxSelected>>', 
                   lambda e, v=item_var, s=slot_frame, l=current_item_label: 
                   on_loadout_item_select(e, v, s, l))
    
    # Update current item label when selection changes
    def update_current_item(*args):
        update_loadout_item_label(current_item_label, item_var)
        update_loadout_slot_border(slot_frame, item_var)
    
    item_var.trace('w', update_current_item)
    
    # Add to loadout entries list
    loadout_entries.append((item_var, count_entry, current_item_label))

# Add this after the update_current_item_label function
def update_loadout_item_label(label, item_var):
    # Get the current item
    current_item = item_var.get()
    label.configure(text=current_item)

root.mainloop()
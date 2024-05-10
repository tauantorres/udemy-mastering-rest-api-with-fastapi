# =============================================================================
#                               REGION: TESTE 01
# =============================================================================

post_table = {
    0: {"id": 0, "body": "The post 0"}
}

def find_post(post_id):
    return post_table.get(post_id)

post = {
    "body": "teste"
}

data = dict(post)
print(data)

last_record_id = len(post_table)
print(last_record_id)

new_post = {**data, "id": last_record_id}
print(new_post)

post_table[last_record_id] = new_post
print(post_table)

print(list(post_table.values()))

outro_post = {
    "body": "teste2"
}

data = dict(outro_post)
print(data)

last_record_id = len(post_table)
print(last_record_id)

new_post = {**data, "id": last_record_id}
print(new_post)

post_table[last_record_id] = new_post
print(post_table)

print(list(post_table.values()))


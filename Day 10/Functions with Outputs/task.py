def format_name(f_name, l_name):
    title_f_name = f_name.title()
    title_l_name = l_name.title()

    return f"{title_f_name} {title_l_name}"

titled_name = format_name("hans", "wurst")

print(titled_name)

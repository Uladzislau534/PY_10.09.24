import copy


site_template = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iPhone',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}


def main():
  
    num_sites = int(input("Сколько сайтов: "))

   
    sites = []

    
    for i in range(num_sites):
        product_name = input("Введите название продукта для нового сайта: ")

   
        new_site = copy.deepcopy(site_template)

      
        new_site['html']['head']['title'] = f'Куплю/продам {product_name} недорого'
        new_site['html']['body']['h2'] = f'У нас самая низкая цена на {product_name}'

      
        sites.append({product_name: new_site})

       
        for site in sites:
            for name, data in site.items():
                print(f"Сайт для {name}:")
                print(f"site = {data}")
                print()

main()


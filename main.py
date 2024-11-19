from random import randint

import click

from utils.style import info_box
from utils.files import write_to_file


@click.group()
def gen():
    pass


@gen.command(help = "Gera números de CPF")
@click.option(
    "-p/-np",
    "--ponctuation/--no-ponctuation",
    help = "Controla se o CPF vai ser gerado com ou sem pontuação", 
    default = True,
    show_default = True
)
@click.option(
    "-g", "--generate",
    help = "Controla quantos CPFs serão gerados",
    default = 1,
    show_default = True
)
@click.option(
    "-o", "--output-file",
    help = "Controla qual será o arquivo de saída (output)",
    default = None
)
def cpf(ponctuation: bool, generate: int, output_file: str):
    if generate < 1: raise click.UsageError("'-g' / '--generate' deve ser maior ou igual a 1")
    
    if output_file != None: cpf_list: list[str] = []

    for _ in range(generate):
        cpf_chars: list[str]

        while True:
            cpf_nums: list[int] = [randint(0, 9) for _ in range(9)]

            if cpf_nums != cpf_nums[::-1]: break

        for i in range(10, 12):
            digit_sum: int = 0

            for j in range(len(cpf_nums)):
                digit_sum += cpf_nums[j] * (i - j)
                
            digit: int = (digit_sum * 10) % 11

            cpf_nums.append(digit if digit != 10 else 0)

        cpf_chars = [str(num) for num in cpf_nums]
        cpf_str: str = "".join(cpf_chars)

        if output_file == None and ponctuation: 
            click.echo(f"\"{cpf_str[0:3]}.{cpf_str[3:6]}.{cpf_str[6:9]}-{cpf_str[9:11]}\"")
        elif output_file == None: 
            click.echo(f"\"{cpf_str}\"")
        elif output_file != None and ponctuation: 
            cpf_list.append(f"\"{cpf_str[0:3]}.{cpf_str[3:6]}.{cpf_str[6:9]}-{cpf_str[9:11]}\"")
        elif output_file != None:
            cpf_list.append(f"\"{cpf_str}\"")

    if output_file != None: 
        write_to_file(output_file, cpf_list)
        info_box("Tudo certo!", f"Os CPFs foram salvos em: {output_file}" if generate > 1 else f"O CPF foi salvo em: {output_file}")


@gen.command(help = "Gera números de CNPJ")
@click.option(
    "-p/-np",
    "--ponctuation/--no-ponctuation",
    help = "Controla se o CNPJ será gerado com ou sem pontuação", 
    default = True,
    show_default = True
)
@click.option(
    "-g", "--generate",
    help = "Controla quantos CNPJs serão gerados",
    default = 1,
    show_default = True
)
@click.option(
    "-o", "--output-file",
    help = "Controla qual será o arquivo de saída (output)",
    default = None
)
def cnpj(ponctuation: bool, generate: int, output_file: str):
    if generate < 1: raise click.UsageError("'-g' / '--generate' deve ser maior ou igual a 1")

    if output_file != None: cnpj_list: list[str] = []

    for _ in range(generate):
        cnpj_chars: list[str]

        while True:
            cnpj_nums: list[int] = [randint(0, 9) for _ in range(8)]

            if cnpj_nums != cnpj_nums[::-1]: 
                cnpj_nums.extend([0, 0, 0, 1])

                break

        for i in range(12, 14):
            digit_sum: int = 0
            multiplier: int = 5 if i == 12 else 6

            for j in range(len(cnpj_nums)):
                digit_sum += cnpj_nums[j] * multiplier

                multiplier -= 1

                multiplier = 9 if multiplier < 2 else multiplier

            cnpj_nums.append(11 - (digit_sum % 11) if digit_sum % 11 >= 2 else 0)

        cnpj_chars: list[str] = [str(num) for num in cnpj_nums]
        cnpj_str: str = "".join(cnpj_chars)

        if output_file == None and ponctuation:
            click.echo(f"\"{cnpj_str[0:2]}.{cnpj_str[2:5]}.{cnpj_str[5:8]}/{cnpj_str[8:12]}-{cnpj_str[12:14]}\"")
        elif output_file == None:
            click.echo(f"\"{cnpj_str}\"")
        elif output_file != None and ponctuation:
            cnpj_list.append(f"\"{cnpj_str[0:2]}.{cnpj_str[2:5]}.{cnpj_str[5:8]}/{cnpj_str[8:12]}-{cnpj_str[12:14]}\"")
        elif output_file != None:
            cnpj_list.append(f"\"{cnpj_str}\"")

    if output_file != None: 
        write_to_file(output_file, cnpj_list)
        info_box("Tudo certo!", f"Os CNPJs foram salvos em: {output_file}" if generate > 1 else f"O CNPJ foi salvo em: {output_file}")


if __name__ == "__main__":
    gen()

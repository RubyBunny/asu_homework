import click

from libs.cipher import Cipher, Mode
from libs.file_reader import FileReader


CONTEXT_DEFAULT = dict(
    default_map={"input": "./input.txt", "output": "./output.txt"})


@click.group(context_settings=CONTEXT_DEFAULT)
@click.option("-i", "--input", default="./input.txt", type=str)
@click.option("-o", "--output", default="./output.txt", type=str)
@click.pass_context
def main(ctx, input: str, output: str):
    ctx.ensure_object(dict)

    ctx.obj["input"] = input
    ctx.obj["output"] = output


@main.command()
@click.option("-k", "--key", required=True, type=int)
@click.option("-e", "--encode", "cipher_mode", flag_value=Mode.encode, type=Mode)
@click.option("-d", "--decode", "cipher_mode", flag_value=Mode.decode, type=Mode)
@click.pass_context
def caesar(ctx: click.Context, key: int, cipher_mode: Mode) -> None:
    original_text = FileReader.get_text_from_file(ctx.obj["input"])
    cipher_text = Cipher.caesar(original_text, key, mode=cipher_mode)
    FileReader.write_text_in_file(ctx.obj["output"], cipher_text)


@main.command()
@click.option("-k", "--key", required=True, type=str)
@click.option("-e", "--encode", "cipher_mode", flag_value=Mode.encode)
@click.option("-d", "--decode", "cipher_mode", flag_value=Mode.decode)
@click.pass_context
def vigener(ctx: click.Context, key: str, cipher_mode: Mode) -> None:
    original_text = FileReader.get_text_from_file(ctx.obj["input"])
    cipher_text = Cipher.vigener(original_text, key, mode=cipher_mode)
    FileReader.write_text_in_file(ctx.obj["output"], cipher_text)


@main.command()
@click.option("-k", "--key", required=True, type=str)
@click.pass_context
def gamming(ctx: click.Context, key: str) -> None:
    original_text = FileReader.get_text_from_file(ctx.obj["input"])
    cipher_text = Cipher.gamming(original_text, key)
    FileReader.write_text_in_file(ctx.obj["output"], cipher_text)


if __name__ == "__main__":
    main()

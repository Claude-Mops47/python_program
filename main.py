# import os
# import send2trash
# import typer
# from pathlib import Path


# def find_files_with_extension(directory: Path, extension: str, sort_order: str = 'asc') -> tuple:
#     """Retourne une liste des fichiers avec l'extension donnée dans le répertoire donné, ainsi que le chemin du dossier."""
#     directory_path = directory
#     # Récupérer la liste des noms de fichiers avec l'extension donnée
#     files = [f.name for f in directory.glob(f"*.{extension}") if f.is_file()]
#     # Trier la liste selon l'ordre alphabétique croissant ou décroissant
#     files.sort(reverse=(sort_order == "desc"))
#     return directory_path, files


# def delete_file(directory_path, file) -> bool:
#     """Supprime un fichier."""
#     chemin = directory_path.joinpath(file)

#     if os.path.exists(chemin):
#         try:
#             send2trash.send2trash(chemin)
#             print(f"Le fichier '{file}' a été envoyé dans la corbeille.")
#             return True
#         except Exception as e:
#             print(
#                 f"Erreur lors de la mise a la corbeille du fichier '{file}': {e}")
#             return False
#     else:
#         print(f"Le fichier '{file}' n'existe pas.")


# def delete_files(directory_path, files: list[str], confirm: bool = False) -> None:
#     """Supprime tous les fichiers de la liste."""
#     # Afficher une liste des fichiers à supprimer
#     print("Fichiers à supprimer :")
#     for file in files:
#         path = Path(file)
#         if confirm:
#             prompt = input(
#                 f"Voulez-vous supprimer le fichier '{path}' ? [O/n] ")
#             if prompt.lower() != "o":
#                 continue
#         delete_file(directory_path, path)


# def main(
#     extension: str,
#     directory: Path = Path.cwd(),
#     delete: bool = False,
#     file: Path = None,
#     confirm: bool = False,
#     sort_order: str = 'asc'


# ) -> None:
#     """
#     Afficher les fichiers trouvés avec l'extension donnée et les supprimer si demandé.

#     Args:\n
#         extension: L'extension des fichiers à chercher.
#         directory: Le répertoire dans lequel chercher les fichiers.
#         delete: Si vrai, supprime les fichiers trouvés sans confirmation.
#         file: Le fichier à supprimer (ignoré si delete est vrai).
#         confirm: Si vrai, demande une confirmation avant de supprimer chaque fichier.
#         sort_order: L'ordre de tri des fichiers ("asc" pour croissant, "desc" pour décroissant)


#     Exemple: python mon_programme.py --extension txt --directory /chemin/vers/dossier --delete --confirm --sort_order desc

#     """
#     if file:
#         delete_file(directory_path, file)
#         return

#     if not directory.is_dir():
#         raise typer.BadParameter(f"Le dossier '{directory}' n'existe pas.")

#     directory_path, files = find_files_with_extension(directory, extension)

#     if files:
#         print(
#             f"Il y a '{len(files)}' fichiers portant l'extension '{extension}' dans le dossier '{directory}', qui sont :")
#         print('\n'.join(files))
#     else:
#         print(
#             f"Aucun fichier avec l'extension '{extension}' trouvé dans le dossier '{directory}'.")

#     if delete:
#         delete_files(directory_path, files, confirm)


# if __name__ == "__main__":
#     typer.run(main)


import os
import send2trash
import typer
from pathlib import Path
import random


def find_files_with_extension(directory: Path, extension: str, sort_order: str = 'asc') -> tuple:
    """Retourne une liste des fichiers avec l'extension donnée dans le répertoire donné, ainsi que le chemin du dossier."""
    if not directory.is_dir():
        raise typer.BadParameter(f"Le dossier '{directory}' n'existe pas.")

    # Vérifier que l'extension est valide
    if not extension:
        raise typer.BadParameter("L'extension doit être spécifiée.")
    elif not extension.startswith("."):
        extension = f".{extension}"

    # Récupérer la liste des noms de fichiers avec l'extension donnée
    files = [f.name for f in directory.glob(f"*{extension}") if f.is_file()]
    if not files:
        raise typer.BadParameter(
            f"Aucun fichier avec l'extension '{extension}' trouvé dans le dossier '{directory}'.")

    # Trier la liste selon l'ordre alphabétique croissant ou décroissant
    if sort_order == "asc":
        files.sort()
    elif sort_order == "desc":
        files.sort(reverse=True)
    elif sort_order == "random":
        random.shuffle(files)
    else:
        raise typer.BadParameter(
            "L'ordre de tri doit être 'asc', 'desc' ou 'random'.")
    return directory, files


def delete_file(directory_path, file) -> bool:
    """Supprime un fichier."""
    chemin = directory_path.joinpath(file)

    if not os.path.exists(chemin):
        print(f"Le fichier '{file}' n'existe pas.")
        return False

    try:
        send2trash.send2trash(chemin)
        print(f"Le fichier '{file}' a été envoyé dans la corbeille.")
        return True
    except Exception as e:
        print(
            f"Erreur lors de la mise a la corbeille du fichier '{file}': {e}")
        return False


def delete_files(directory_path, files: list[str], confirm: bool = False) -> None:
    """Supprime tous les fichiers de la liste."""
    # Afficher une liste des fichiers à supprimer
    print("Fichiers à supprimer :")
    for file in files:
        path = Path(file)
        if confirm:
            prompt = input(
                f"Voulez-vous supprimer le fichier '{path}' ? [O/n] ")
            if prompt.lower() != "o":
                continue
        delete_file(directory_path, path)


def display_files_content(directory_path, files: list[str], confirm: bool = False) -> None:
    """Affiche le contenu des fichiers de la liste"""
    for file in files:
        path = directory_path.joinpath(file)
        if not path.exists():
            print("Le fichier '{file}' n'existe pas.")
            continue

        # Afficher le contenu du fichier
        print(f"Contenu du fichier '{file}' :")
        try:
            with open(path, 'r') as f:
                content = f.read()
                print(content)
        except Exception as e:
            print(f"Erreur lors de la lecture du fichier '{file}': {e}")
            continue


def main(directory: str, extension: str, delete: bool = False, display_content: bool = False,
         confirm: bool = False, sort_order: str = 'asc') -> None:
    """Fonction principale."""
    directory_path = Path(directory)
    directory, files = find_files_with_extension(
        directory_path, extension, sort_order)
    if delete:
        delete_files(directory_path, files, confirm)
    elif display_content:
        display_files_content(directory_path, files, confirm)


if __name__ == "__main__":
    typer.run(main)

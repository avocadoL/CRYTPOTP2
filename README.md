# Implémentation du DES (Data Encryption Standard)

Cette implémentation Python de l'algorithme de chiffrement DES (Data Encryption Standard) suit les spécifications standard et inclut tous les composants nécessaires de l'algorithme DES.

## Fonctionnalités

1. Conversion Texte-Binaire
   - Conversion du texte ASCII en représentation binaire
   - Conversion du binaire en texte ASCII

2. Initialisation des Blocs
   - Traitement du texte en blocs de 64 bits
   - Remplissage automatique pour les blocs incomplets

3. Composants DES
   - Permutation Initiale (IP)
   - Permutation Initiale Inverse (IP^-1)
   - Expansion (E)
   - Permutation P-Box (P)
   - Boîtes de Substitution (8 S-boxes)
   - Génération des Sous-clés (PC1 et PC2)

4. Fonctions Principales
   - Implémentation du réseau de Feistel
   - 16 rounds de chiffrement/déchiffrement
   - Génération des sous-clés
   - Chiffrement et déchiffrement par blocs

5. Interface Utilisateur
   - Interface en ligne de commande interactive
   - Support pour le chiffrement et le déchiffrement
   - Gestion des erreurs

## Fichiers

- `des.py` : Implémentation principale de l'algorithme DES
- `main.py` : Interface utilisateur pour le chiffrement/déchiffrement
- `README.md` : Documentation

## Utilisation

1. Exécuter le programme :
   ```bash
   python main.py
   ```

2. Choisir une opération :
   - 1 : Chiffrer un message
   - 2 : Déchiffrer un message
   - 3 : Quitter

3. Pour le chiffrement :
   - Entrez le texte à chiffrer
   - Entrez une clé de chiffrement (sera complétée/tronquée à 8 caractères)
   - Le programme affichera la chaîne binaire chiffrée

4. Pour le déchiffrement :
   - Entrez la chaîne binaire à déchiffrer
   - Entrez la même clé utilisée pour le chiffrement
   - Le programme affichera le texte déchiffré

## Détails d'Implémentation

### Caractéristiques Principales

1. **Conception Modulaire** : Le code est organisé en modules séparés pour les fonctionnalités principales et l'interface utilisateur.
2. **Gestion des Erreurs** : Gestion robuste des entrées invalides et des erreurs de traitement.
3. **Gestion des Clés** : Remplissage/troncature automatique pour assurer une longueur de clé de 64 bits.
4. **Conformité aux Standards** : Implémente tous les composants DES selon la spécification.

### Notes de Sécurité

1. L'implémentation utilise les tables et permutations DES standard.
2. Les clés sont traitées pour avoir exactement 8 caractères (64 bits).
3. Cette implémentation est à but éducatif et ne doit pas être utilisée en production.

## Exemple

```python
# Chiffrement
plaintext = "Hello!"
key = "secret"
encrypted = des_encrypt(plaintext, key)

# Déchiffrement
decrypted = des_decrypt(encrypted, key)
# Résultat : "Hello!"
```

## Prérequis

- Python 3.6 ou supérieur
- Aucune dépendance externe requise

## Limitations

1. Cette implémentation est en Python pur, elle peut donc être moins rapide que les implémentations optimisées.
2. L'implémentation privilégie la clarté et la lisibilité plutôt que la performance.
3. DES est considéré comme cryptographiquement faible selon les standards modernes et ne doit pas être utilisé pour des communications sécurisées.

## Licence

Ce code est fourni à des fins éducatives uniquement. Utilisation à vos propres risques. 
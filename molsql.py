import os
import sqlite3

if os.path.exists('test.db'):
    os.remove('test.db')

# create database file if it doesn't exist and connect to it
conn = sqlite3.connect('test.db')

# Element Table
conn.execute("""CREATE TABLE Elements 
                 ( ELEMENT_NO   INTEGER     NOT NULL,
                   ELEMENT_CODE VARCHAR(3)  NOT NULL    PRIMARY KEY,
                   ELEMENT_NAME VARCHAR(32) NOT NULL,
                   COLOUR1      CHAR(6)     NOT NULL,
                   COLOUR2      CHAR(6)     NOT NULL,
                   COLOUR3      CHAR(6)     NOT NULL,
                   RADIUS       DECIMAL(3)  NOT NULL);""")

# Atom Table
conn.execute("""CREATE TABLE Atoms 
                 ( ATOM_ID      INTEGER         NOT NULL    PRIMARY KEY     AUTOINCREMENT,
                   ELEMENT_CODE VARCHAR(3)      NOT NULL,
                   ELEMENT_NAME VARCHAR(32)     NOT NULL,
                   x            DECIMAL(7,4)    NOT NULL,
                   y            DECIMAL(7,4)    NOT NULL,
                   z            DECIMAL(7,4)    NOT NULL,
                   FOREIGN KEY (ELEMENT_CODE) REFERENCES Elements);""")


# Bond Table
conn.execute("""CREATE TABLE Bonds 
                 ( BOND_ID      INTEGER     NOT NULL    PRIMARY KEY     AUTOINCREMENT,
                   A1           INTEGER     NOT NULL,
                   A2           INTEGER     NOT NULL,
                   EPAIRS       INTEGER     NOT NULL);""")

# Molecules Table
conn.execute("""CREATE TABLE Molecules 
                 ( MOLECULE_ID  INTEGER     NOT NULL    PRIMARY KEY     AUTOINCREMENT,
                   NAME         TEXT        NOT NULL    UNIQUE);""")

# MoleculeAtom Table
conn.execute("""CREATE TABLE MoleculeAtom 
                 ( MOLECULE_ID  INTEGER     NOT NULL,
                   ATOM_ID      INTEGER     NOT NULL,
                   PRIMARY KEY  (MOLECULE_ID, ATOM_ID),
                   FOREIGN KEY (MOLECULE_ID) REFERENCES Molecules,
                   FOREIGN KEY (ATOM_ID) REFERENCES Atoms);""")

# MoleculeBond Table
conn.execute("""CREATE TABLE MoleculeBond 
                 ( MOLECULE_ID  INTEGER     NOT NULL,
                   BOND_ID      INTEGER     NOT NULL,
                   PRIMARY KEY  (MOLECULE_ID, BOND_ID),
                   FOREIGN KEY (MOLECULE_ID) REFERENCES Molecules,
                   FOREIGN KEY (BOND_ID) REFERENCES Bonds);""")
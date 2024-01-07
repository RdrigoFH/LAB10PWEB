#!/usr/bin/perl
use strict;
use warnings;
use CGI;
use DBI;

# CGI Initialization
my $cgi = CGI->new;

# Database Connection Parameters
my $servername = "localhost";
my $username = "root";
my $password = "contrasena";
my $database = "movies";

# Connect to the database
my $dbh = DBI->connect("DBI:mysql:database=$database;host=$servername", $username, $password, { PrintError => 0, RaiseError => 1 });

# Check for database connection errors
if (!$dbh) {
    print $cgi->header(-type => 'text/html', -status => '500 Internal Server Error');
    die "Conexión fallida: " . DBI::errstr;
}
$dbh->disconnect();

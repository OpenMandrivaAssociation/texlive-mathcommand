%global tl_name mathcommand
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.04
Release:	%{tl_revision}.1
Summary:	\newcommand-like commands for defining math macros
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mathcommand
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathcommand.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathcommand.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathcommand.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides functionalities for defining macros that have
different behaviors depending on whether in math or text mode, that
absorb Primes, Indices and Exponents (PIE) as extra parameters usable in
the code; and it offers some iteration facilities for defining macros
with similar code. The primary objective of this package is to be used
together with the knowledge package for a proper handling of
mathematical notations.


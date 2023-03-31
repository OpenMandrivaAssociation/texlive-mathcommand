Name:		texlive-mathcommand
Version:	59512
Release:	2
Summary:	\newcommand-like commands for defining math macros
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mathcommand
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathcommand.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathcommand.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathcommand.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides functionalities for defining macros that
have different behaviors depending on whether in math or text
mode, that absorb Primes, Indices and Exponents (PIE) as extra
parameters usable in the code; and it offers some iteration
facilities for defining macros with similar code. The primary
objective of this package is to be used together with the
knowledge package for a proper handling of mathematical
notations.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/mathcommand
%{_texmfdistdir}/tex/latex/mathcommand
%doc %{_texmfdistdir}/doc/latex/mathcommand

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

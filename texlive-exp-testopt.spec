Name:		texlive-exp-testopt
Version:	15878
Release:	2
Summary:	Expandable \@testopt (and related) macros
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/exp-testopt
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exp-testopt.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exp-testopt.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exp-testopt.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides an expandable variant of the LaTeX kernel
command \@testopt, named \@expandable@testopt, and a more
general \@expandable@ifopt, both intended for package writers.
Also we have a variant of \newcommand which uses these macros
to check for optional arguments.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/exp-testopt/exp-testopt.sty
%doc %{_texmfdistdir}/doc/latex/exp-testopt/README
%doc %{_texmfdistdir}/doc/latex/exp-testopt/exp-testopt.pdf
%doc %{_texmfdistdir}/doc/latex/exp-testopt/exp-testopt.test
#- source
%doc %{_texmfdistdir}/source/latex/exp-testopt/exp-testopt.dtx
%doc %{_texmfdistdir}/source/latex/exp-testopt/exp-testopt.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

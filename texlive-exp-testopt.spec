# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/exp-testopt
# catalog-date 2009-03-08 17:38:29 +0100
# catalog-license lppl
# catalog-version 0.3
Name:		texlive-exp-testopt
Version:	0.3
Release:	1
Summary:	Expandable \@testopt (and related) macros
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/exp-testopt
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exp-testopt.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exp-testopt.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exp-testopt.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides an expandable variant of the LaTeX kernel
command \@testopt, named \@expandable@testopt, and a more
general \@expandable@ifopt, both intended for package writers.
Also we have a variant of \newcommand which uses these macros
to check for optional arguments.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}

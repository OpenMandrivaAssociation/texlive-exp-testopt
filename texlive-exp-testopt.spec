%global tl_name exp-testopt
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3
Release:	%{tl_revision}.1
Summary:	Expandable \@testopt (and related) macros
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/exp-testopt
License:	lppl1.3b
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/exp-testopt.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/exp-testopt.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/exp-testopt.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides an expandable variant of the LaTeX kernel command
\@testopt, named \@expandable@testopt, and a more general
\@expandable@ifopt, both intended for package writers. Also we have a
variant of \newcommand which uses these macros to check for optional
arguments.


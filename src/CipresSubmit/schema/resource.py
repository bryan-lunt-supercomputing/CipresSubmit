# ./resource.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:c6d1b822a1552c7c3e6a47edb3eca29b0d3d32d1
# Generated 2014-02-02 16:38:24.673937 by PyXB version 1.2.3
# Namespace http://www.phylog.org/submit/resource

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:7d7d0a45-8c6b-11e3-ab86-002241226b3f')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.3'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://www.phylog.org/submit/resource', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, unicode):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 73, 7)
    _Documentation = None
STD_ANON._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON, value=pyxb.binding.datatypes.int(1))
STD_ANON._InitializeFacetMap(STD_ANON._CF_minInclusive)

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 81, 7)
    _Documentation = None
STD_ANON_._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_, value=pyxb.binding.datatypes.int(1))
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_minInclusive)

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 88, 7)
    _Documentation = None
STD_ANON_2._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_2, value=pyxb.binding.datatypes.int(1))
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_minInclusive)

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.float):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 95, 7)
    _Documentation = None
STD_ANON_3._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_3, value=pyxb.binding.datatypes.float(0.0))
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_minInclusive)

# Atomic simple type: [anonymous]
class STD_ANON_4 (pyxb.binding.datatypes.float):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 124, 9)
    _Documentation = None
STD_ANON_4._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_4, value=pyxb.binding.datatypes.float(0.0))
STD_ANON_4._InitializeFacetMap(STD_ANON_4._CF_minInclusive)

# Complex type {http://www.phylog.org/submit/resource}ResourceType with content type ELEMENT_ONLY
class ResourceType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.phylog.org/submit/resource}ResourceType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ResourceType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 5, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.phylog.org/submit/resource}hosts uses Python identifier hosts
    __hosts = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'hosts'), 'hosts', '__httpwww_phylog_orgsubmitresource_ResourceType_httpwww_phylog_orgsubmitresourcehosts', False, pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 7, 6), )

    
    hosts = property(__hosts.value, __hosts.set, None, None)

    
    # Element {http://www.phylog.org/submit/resource}account uses Python identifier account
    __account = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'account'), 'account', '__httpwww_phylog_orgsubmitresource_ResourceType_httpwww_phylog_orgsubmitresourceaccount', False, pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 22, 6), )

    
    account = property(__account.value, __account.set, None, None)

    
    # Element {http://www.phylog.org/submit/resource}batch-system uses Python identifier batch_system
    __batch_system = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'batch-system'), 'batch_system', '__httpwww_phylog_orgsubmitresource_ResourceType_httpwww_phylog_orgsubmitresourcebatch_system', False, pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 25, 6), )

    
    batch_system = property(__batch_system.value, __batch_system.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpwww_phylog_orgsubmitresource_ResourceType_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 29, 5)
    __name._UseLocation = pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 29, 5)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __hosts.name() : __hosts,
        __account.name() : __account,
        __batch_system.name() : __batch_system
    })
    _AttributeMap.update({
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', u'ResourceType', ResourceType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 8, 7)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.phylog.org/submit/resource}host uses Python identifier host
    __host = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'host'), 'host', '__httpwww_phylog_orgsubmitresource_CTD_ANON_httpwww_phylog_orgsubmitresourcehost', True, pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 10, 9), )

    
    host = property(__host.value, __host.set, None, None)

    _ElementMap.update({
        __host.name() : __host
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 12, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute pattern uses Python identifier pattern
    __pattern = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'pattern'), 'pattern', '__httpwww_phylog_orgsubmitresource_CTD_ANON__pattern', pyxb.binding.datatypes.string)
    __pattern._DeclarationLocation = pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 13, 11)
    __pattern._UseLocation = pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 13, 11)
    
    pattern = property(__pattern.value, __pattern.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpwww_phylog_orgsubmitresource_CTD_ANON__name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 16, 11)
    __name._UseLocation = pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 16, 11)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __pattern.name() : __pattern,
        __name.name() : __name
    })



# Complex type {http://www.phylog.org/submit/resource}AccountType with content type ELEMENT_ONLY
class AccountType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.phylog.org/submit/resource}AccountType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AccountType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 35, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.phylog.org/submit/resource}accountstr uses Python identifier accountstr
    __accountstr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'accountstr'), 'accountstr', '__httpwww_phylog_orgsubmitresource_AccountType_httpwww_phylog_orgsubmitresourceaccountstr', True, pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 37, 6), )

    
    accountstr = property(__accountstr.value, __accountstr.set, None, None)

    _ElementMap.update({
        __accountstr.name() : __accountstr
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'AccountType', AccountType)


# Complex type {http://www.phylog.org/submit/resource}batch-systemType with content type ELEMENT_ONLY
class batch_systemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.phylog.org/submit/resource}batch-systemType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'batch-systemType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 41, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.phylog.org/submit/resource}templates uses Python identifier templates
    __templates = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'templates'), 'templates', '__httpwww_phylog_orgsubmitresource_batch_systemType_httpwww_phylog_orgsubmitresourcetemplates', False, pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 43, 6), )

    
    templates = property(__templates.value, __templates.set, None, None)

    
    # Element {http://www.phylog.org/submit/resource}queues uses Python identifier queues
    __queues = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'queues'), 'queues', '__httpwww_phylog_orgsubmitresource_batch_systemType_httpwww_phylog_orgsubmitresourcequeues', False, pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 50, 6), )

    
    queues = property(__queues.value, __queues.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpwww_phylog_orgsubmitresource_batch_systemType_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 57, 5)
    __type._UseLocation = pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 57, 5)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        __templates.name() : __templates,
        __queues.name() : __queues
    })
    _AttributeMap.update({
        __type.name() : __type
    })
Namespace.addCategoryObject('typeBinding', u'batch-systemType', batch_systemType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 44, 7)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.phylog.org/submit/resource}template uses Python identifier template
    __template = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'template'), 'template', '__httpwww_phylog_orgsubmitresource_CTD_ANON_2_httpwww_phylog_orgsubmitresourcetemplate', True, pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 46, 9), )

    
    template = property(__template.value, __template.set, None, None)

    _ElementMap.update({
        __template.name() : __template
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 51, 7)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.phylog.org/submit/resource}queue uses Python identifier queue
    __queue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'queue'), 'queue', '__httpwww_phylog_orgsubmitresource_CTD_ANON_3_httpwww_phylog_orgsubmitresourcequeue', True, pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 53, 9), )

    
    queue = property(__queue.value, __queue.set, None, None)

    _ElementMap.update({
        __queue.name() : __queue
    })
    _AttributeMap.update({
        
    })



# Complex type {http://www.phylog.org/submit/resource}TemplateType with content type ELEMENT_ONLY
class TemplateType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.phylog.org/submit/resource}TemplateType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TemplateType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 61, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.phylog.org/submit/resource}param uses Python identifier param
    __param = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'param'), 'param', '__httpwww_phylog_orgsubmitresource_TemplateType_httpwww_phylog_orgsubmitresourceparam', True, pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 63, 6), )

    
    param = property(__param.value, __param.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpwww_phylog_orgsubmitresource_TemplateType_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 65, 5)
    __name._UseLocation = pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 65, 5)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute filename uses Python identifier filename
    __filename = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'filename'), 'filename', '__httpwww_phylog_orgsubmitresource_TemplateType_filename', pyxb.binding.datatypes.string)
    __filename._DeclarationLocation = pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 66, 5)
    __filename._UseLocation = pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 66, 5)
    
    filename = property(__filename.value, __filename.set, None, None)

    _ElementMap.update({
        __param.name() : __param
    })
    _AttributeMap.update({
        __name.name() : __name,
        __filename.name() : __filename
    })
Namespace.addCategoryObject('typeBinding', u'TemplateType', TemplateType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 102, 7)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.phylog.org/submit/resource}env uses Python identifier env
    __env = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'env'), 'env', '__httpwww_phylog_orgsubmitresource_CTD_ANON_4_httpwww_phylog_orgsubmitresourceenv', True, pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 104, 9), )

    
    env = property(__env.value, __env.set, None, None)

    _ElementMap.update({
        __env.name() : __env
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 112, 7)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.phylog.org/submit/resource}property uses Python identifier property_
    __property = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'property'), 'property_', '__httpwww_phylog_orgsubmitresource_CTD_ANON_5_httpwww_phylog_orgsubmitresourceproperty', True, pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 114, 9), )

    
    property_ = property(__property.value, __property.set, None, None)

    _ElementMap.update({
        __property.name() : __property
    })
    _AttributeMap.update({
        
    })



# Complex type {http://www.phylog.org/submit/resource}envType with content type SIMPLE
class envType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.phylog.org/submit/resource}envType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'envType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 134, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpwww_phylog_orgsubmitresource_envType_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 137, 7)
    __name._UseLocation = pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 137, 7)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', u'envType', envType)


# Complex type {http://www.phylog.org/submit/resource}TemplateParamType with content type SIMPLE
class TemplateParamType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.phylog.org/submit/resource}TemplateParamType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TemplateParamType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 142, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpwww_phylog_orgsubmitresource_TemplateParamType_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 145, 7)
    __name._UseLocation = pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 145, 7)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', u'TemplateParamType', TemplateParamType)


# Complex type {http://www.phylog.org/submit/resource}queueType with content type ELEMENT_ONLY
class queueType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.phylog.org/submit/resource}queueType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'queueType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 69, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.phylog.org/submit/resource}cores-per-node uses Python identifier cores_per_node
    __cores_per_node = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'cores-per-node'), 'cores_per_node', '__httpwww_phylog_orgsubmitresource_queueType_httpwww_phylog_orgsubmitresourcecores_per_node', False, pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 71, 6), )

    
    cores_per_node = property(__cores_per_node.value, __cores_per_node.set, None, None)

    
    # Element {http://www.phylog.org/submit/resource}cores-increment uses Python identifier cores_increment
    __cores_increment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'cores-increment'), 'cores_increment', '__httpwww_phylog_orgsubmitresource_queueType_httpwww_phylog_orgsubmitresourcecores_increment', False, pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 79, 6), )

    
    cores_increment = property(__cores_increment.value, __cores_increment.set, None, None)

    
    # Element {http://www.phylog.org/submit/resource}max-nodes uses Python identifier max_nodes
    __max_nodes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'max-nodes'), 'max_nodes', '__httpwww_phylog_orgsubmitresource_queueType_httpwww_phylog_orgsubmitresourcemax_nodes', False, pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 87, 6), )

    
    max_nodes = property(__max_nodes.value, __max_nodes.set, None, None)

    
    # Element {http://www.phylog.org/submit/resource}max-run-hours uses Python identifier max_run_hours
    __max_run_hours = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'max-run-hours'), 'max_run_hours', '__httpwww_phylog_orgsubmitresource_queueType_httpwww_phylog_orgsubmitresourcemax_run_hours', False, pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 94, 6), )

    
    max_run_hours = property(__max_run_hours.value, __max_run_hours.set, None, None)

    
    # Element {http://www.phylog.org/submit/resource}env-vars uses Python identifier env_vars
    __env_vars = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'env-vars'), 'env_vars', '__httpwww_phylog_orgsubmitresource_queueType_httpwww_phylog_orgsubmitresourceenv_vars', False, pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 101, 6), )

    
    env_vars = property(__env_vars.value, __env_vars.set, None, None)

    
    # Element {http://www.phylog.org/submit/resource}node-properties uses Python identifier node_properties
    __node_properties = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'node-properties'), 'node_properties', '__httpwww_phylog_orgsubmitresource_queueType_httpwww_phylog_orgsubmitresourcenode_properties', False, pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 110, 6), )

    
    node_properties = property(__node_properties.value, __node_properties.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpwww_phylog_orgsubmitresource_queueType_id', pyxb.binding.datatypes.string)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 121, 5)
    __id._UseLocation = pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 121, 5)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpwww_phylog_orgsubmitresource_queueType_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 122, 5)
    __name._UseLocation = pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 122, 5)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute charge-factor uses Python identifier charge_factor
    __charge_factor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'charge-factor'), 'charge_factor', '__httpwww_phylog_orgsubmitresource_queueType_charge_factor', STD_ANON_4, unicode_default=u'1.0')
    __charge_factor._DeclarationLocation = pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 123, 5)
    __charge_factor._UseLocation = pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 123, 5)
    
    charge_factor = property(__charge_factor.value, __charge_factor.set, None, None)

    _ElementMap.update({
        __cores_per_node.name() : __cores_per_node,
        __cores_increment.name() : __cores_increment,
        __max_nodes.name() : __max_nodes,
        __max_run_hours.name() : __max_run_hours,
        __env_vars.name() : __env_vars,
        __node_properties.name() : __node_properties
    })
    _AttributeMap.update({
        __id.name() : __id,
        __name.name() : __name,
        __charge_factor.name() : __charge_factor
    })
Namespace.addCategoryObject('typeBinding', u'queueType', queueType)


resource = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'resource'), ResourceType, location=pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 150, 4))
Namespace.addCategoryObject('elementBinding', resource.name().localName(), resource)



ResourceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'hosts'), CTD_ANON, scope=ResourceType, location=pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 7, 6)))

ResourceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'account'), AccountType, scope=ResourceType, location=pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 22, 6)))

ResourceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'batch-system'), batch_systemType, scope=ResourceType, location=pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 25, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 22, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ResourceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'hosts')), pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 7, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ResourceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'account')), pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 22, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ResourceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'batch-system')), pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 25, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ResourceType._Automaton = _BuildAutomaton()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'host'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 10, 9)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'host')), pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 10, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_()




AccountType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accountstr'), pyxb.binding.datatypes.string, scope=AccountType, location=pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 37, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 37, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AccountType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'accountstr')), pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 37, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AccountType._Automaton = _BuildAutomaton_2()




batch_systemType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'templates'), CTD_ANON_2, scope=batch_systemType, location=pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 43, 6)))

batch_systemType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'queues'), CTD_ANON_3, scope=batch_systemType, location=pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 50, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(batch_systemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'templates')), pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 43, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(batch_systemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'queues')), pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 50, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
batch_systemType._Automaton = _BuildAutomaton_3()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'template'), TemplateType, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 46, 9)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 46, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'template')), pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 46, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_4()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'queue'), queueType, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 53, 9)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 53, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'queue')), pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 53, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_5()




TemplateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'param'), TemplateParamType, scope=TemplateType, location=pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 63, 6)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 63, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TemplateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'param')), pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 63, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TemplateType._Automaton = _BuildAutomaton_6()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'env'), envType, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 104, 9)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 104, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'env')), pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 104, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_7()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'property'), pyxb.binding.datatypes.string, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 114, 9)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 114, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'property')), pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 114, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_8()




queueType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cores-per-node'), STD_ANON, scope=queueType, location=pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 71, 6)))

queueType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cores-increment'), STD_ANON_, scope=queueType, location=pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 79, 6)))

queueType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'max-nodes'), STD_ANON_2, scope=queueType, location=pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 87, 6)))

queueType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'max-run-hours'), STD_ANON_3, scope=queueType, location=pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 94, 6)))

queueType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'env-vars'), CTD_ANON_4, scope=queueType, location=pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 101, 6)))

queueType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'node-properties'), CTD_ANON_5, scope=queueType, location=pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 110, 6)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 79, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 87, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 94, 6))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(queueType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cores-per-node')), pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 71, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(queueType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cores-increment')), pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 79, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(queueType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'max-nodes')), pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 87, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(queueType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'max-run-hours')), pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 94, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(queueType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'env-vars')), pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 101, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(queueType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'node-properties')), pyxb.utils.utility.Location('/Users/lunt/Documents/SDSClocal/EclipseWorkspaces/parallelWS/CipresSubmit/src/CipresSubmit/schema/resource.xsd', 110, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
queueType._Automaton = _BuildAutomaton_9()

